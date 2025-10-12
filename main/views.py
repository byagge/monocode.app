from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
import requests
import json


def home(request):
    """Главная страница"""
    return render(request, 'main/home.html')


def about(request):
    """Страница О нас"""
    return render(request, 'main/about.html')


def contact(request):
    """Страница Контакты"""
    return render(request, 'main/contact.html')


@csrf_exempt
@require_http_methods(["POST"])
def send_contact_form(request):
    """Отправка формы контактов в Telegram"""
    try:
        # Получаем данные из формы
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        telegram = data.get('telegram', '').strip()
        message = data.get('message', '').strip()
        
        # Валидация
        if not all([name, email, message]):
            return JsonResponse({
                'success': False,
                'message': 'Пожалуйста, заполните все обязательные поля'
            }, status=400)
        
        # Формируем сообщение для Telegram
        telegram_message = f"""
📧 <b>Новое сообщение с сайта</b>

👤 <b>Имя:</b> {name}
📧 <b>Email:</b> {email}
📱 <b>Telegram:</b> {telegram if telegram else 'Не указан'}

💬 <b>Сообщение:</b>
{message}
        """
        
        # Отправляем в Telegram
        telegram_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
        admin_chat_id = getattr(settings, 'TELEGRAM_ADMIN_CHAT_ID', None)
        
        if not telegram_token or not admin_chat_id:
            return JsonResponse({
                'success': False,
                'message': 'Настройки Telegram не найдены'
            }, status=500)
        
        # URL для отправки сообщения в Telegram
        telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        
        payload = {
            'chat_id': admin_chat_id,
            'text': telegram_message,
            'parse_mode': 'HTML'
        }
        
        response = requests.post(telegram_url, data=payload, timeout=5)
        
        if response.status_code == 200:
            return JsonResponse({
                'success': True,
                'message': 'Сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Ошибка при отправке сообщения. Попробуйте позже.'
            }, status=500)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Неверный формат данных'
        }, status=400)
    except requests.RequestException as e:
        return JsonResponse({
            'success': False,
            'message': 'Ошибка соединения. Попробуйте позже.'
        }, status=500)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Произошла ошибка. Попробуйте позже.'
        }, status=500)
