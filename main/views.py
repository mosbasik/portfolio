# django imports
from django.http import Http404
from django.shortcuts import render

# local imports
from main.models import TextBlock, Blog, Project

# python imports
from datetime import datetime
import pytz


def home(request):
    context = {}
    context['blogs'] = Blog.get_ordered(count=3)
    context['projects'] = Project.get_ordered(count=3)

    try:
        context['welcome'] = TextBlock.objects.get(name='welcome')
    except TextBlock.DoesNotExist:
        welcome, created = TextBlock.objects.get_or_create(
            name='_default_welcome',
            body='# Welcome\n\nPage is under development.'
        )
        context['welcome'] = welcome

    return render(request, 'main/home.html', context)


def blog_list(request):
    context = {}
    context['entries'] = Blog.get_ordered()
    return render(request, 'main/blog_list.html', context)


def blog_details(request, year, month, day, entry_slug):
    request_date = datetime(int(year), int(month), int(day))
    entries = Blog.objects.filter(
        display_date__year=request_date.year,
        display_date__month=request_date.month,
        display_date__day=request_date.day,
    )

    try:
        context = {}
        context['entry'] = entries.get(slug=entry_slug)
        return render(request, 'main/blog_details.html', context)

    except Blog.DoesNotExist:
        raise Http404("No entry matches the given query.")


def project_list(request):
    context = {}
    context['entries'] = Project.get_ordered()
    return render(request, 'main/project_list.html', context)


def project_details(request, year, month, day, entry_slug):
    request_date = datetime(int(year), int(month), int(day))
    entries = Project.objects.filter(
        display_date__year=request_date.year,
        display_date__month=request_date.month,
        display_date__day=request_date.day,
    )

    try:
        context = {}
        context['entry'] = entries.get(slug=entry_slug)
        return render(request, 'main/project_details.html', context)

    except Project.DoesNotExist:
        raise Http404("No entry matches the given query.")


def about(request):
    context = {}
    context['contact_info'] = TextBlock.get('contact_info', '## Contact Information')
    context['overview'] = TextBlock.get('overview', '## Overview')
    context['technology'] = TextBlock.get('technology', '## Technology')
    context['leisure'] = TextBlock.get('leisure', '## Leisure')
    return render(request, 'main/about.html', context)
