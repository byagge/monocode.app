from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.html import format_html


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    """Скрыть пункт меню Snippets в админке Wagtail"""
    menu_items[:] = [item for item in menu_items if item.name != 'snippets']


@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Добавить кастомные стили в админку Wagtail"""
    return format_html(
        '<style>'
        '.c-sf-widget { max-width: 100%; }'
        '.field-content img { max-width: 200px; height: auto; }'
        '</style>'
    )
