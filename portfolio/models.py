from django.db import models
from django.urls import reverse


class PortfolioProject(models.Model):
    """Модель проекта портфолио"""
    title = models.CharField(max_length=200, help_text="Название проекта")
    slug = models.SlugField(unique=True, help_text="URL-адрес проекта")
    description = models.TextField(blank=True, help_text="Описание проекта")
    technologies = models.CharField(max_length=255, help_text="Используемые технологии (через запятую)")
    
    # Основное изображение (обложка)
    cover_image = models.ImageField(
        upload_to='portfolio/covers/',
        null=True,
        blank=True,
        help_text="Обложка проекта для списка"
    )
    
    # Детальная информация
    client = models.CharField(max_length=200, blank=True, help_text="Клиент")
    duration = models.CharField(max_length=100, blank=True, help_text="Срок выполнения")
    budget = models.CharField(max_length=100, blank=True, help_text="Бюджет")
    team_size = models.CharField(max_length=100, blank=True, help_text="Размер команды")
    category = models.CharField(max_length=100, blank=True, help_text="Категория проекта")
    
    # Ссылки
    project_url = models.URLField(blank=True, help_text="Ссылка на проект")
    github_url = models.URLField(blank=True, help_text="Ссылка на GitHub")
    
    # Дополнительные изображения для галереи
    gallery_image_1 = models.ImageField(
        upload_to='portfolio/gallery/',
        null=True,
        blank=True,
        help_text="Изображение галереи 1"
    )
    gallery_image_2 = models.ImageField(
        upload_to='portfolio/gallery/',
        null=True,
        blank=True,
        help_text="Изображение галереи 2"
    )
    gallery_image_3 = models.ImageField(
        upload_to='portfolio/gallery/',
        null=True,
        blank=True,
        help_text="Изображение галереи 3"
    )
    gallery_image_4 = models.ImageField(
        upload_to='portfolio/gallery/',
        null=True,
        blank=True,
        help_text="Изображение галереи 4"
    )
    
    # Метаданные
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'slug': self.slug})
    
    def get_gallery_images(self):
        """Возвращает список изображений галереи"""
        images = []
        if self.gallery_image_1:
            images.append(self.gallery_image_1)
        if self.gallery_image_2:
            images.append(self.gallery_image_2)
        if self.gallery_image_3:
            images.append(self.gallery_image_3)
        if self.gallery_image_4:
            images.append(self.gallery_image_4)
        return images

    class Meta:
        verbose_name = "Проект портфолио"
        verbose_name_plural = "Проекты портфолио"
        ordering = ['-created_at']
