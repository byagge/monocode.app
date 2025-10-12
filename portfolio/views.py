from django.shortcuts import render, get_object_or_404
from .models import PortfolioProject


def portfolio_list(request):
    """Список всех проектов портфолио"""
    projects = PortfolioProject.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {
        'projects': projects
    })


def portfolio_detail(request, slug):
    """Детальная страница проекта портфолио"""
    project = get_object_or_404(PortfolioProject, slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {
        'project': project
    })
