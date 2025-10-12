from django.contrib import admin
from django.utils.html import format_html
from .models import PortfolioProject


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'category', 'duration', 'cover_preview', 'created_at')
    list_filter = ('created_at', 'updated_at', 'category')
    search_fields = ('title', 'client', 'technologies', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'cover_preview')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Информация о проекте', {
            'fields': ('client', 'duration', 'budget', 'team_size')
        }),
        ('Технологии', {
            'fields': ('technologies',)
        }),
        ('Обложка проекта', {
            'fields': ('cover_image', 'cover_preview'),
            'description': 'Изображение, которое будет отображаться в списке проектов'
        }),
        ('Галерея изображений', {
            'fields': ('gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4'),
            'description': 'Дополнительные изображения для детальной страницы проекта'
        }),
        ('Ссылки', {
            'fields': ('project_url', 'github_url'),
            'classes': ('collapse',)
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.cover_image.url)
        return "Нет изображения"
    cover_preview.short_description = "Превью обложки"
