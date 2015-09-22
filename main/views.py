# django imports
from django.http import Http404
from django.shortcuts import render

# local imports
from main.models import BlogEntry, ProjectEntry

# python imports
from datetime import datetime
import pytz


def home(request):
    context = {}
    context['blogs'] = BlogEntry.get_ordered(count=3)
    context['projects'] = ProjectEntry.get_ordered(count=3)
    return render(request, 'main/home.html', context)


def blog_list(request):
    context = {}
    context['entries'] = BlogEntry.get_ordered()
    return render(request, 'main/blog_list.html', context)


def blog_details(request, year, month, day, entry_slug):
    request_date = datetime(int(year), int(month), int(day))
    entries = BlogEntry.objects.filter(
        display_date__year=request_date.year,
        display_date__month=request_date.month,
        display_date__day=request_date.day,
    )

    try:
        context = {}
        context['entry'] = entries.get(slug=entry_slug)
        return render(request, 'main/blog_details.html', context)

    except BlogEntry.DoesNotExist:
        raise Http404("No entry matches the given query.")


def project_list(request):
    context = {}
    context['entries'] = ProjectEntry.get_ordered()
    return render(request, 'main/project_list.html', context)


def project_details(request, year, month, day, entry_slug):
    request_date = datetime(int(year), int(month), int(day))
    entries = ProjectEntry.objects.filter(
        display_date__year=request_date.year,
        display_date__month=request_date.month,
        display_date__day=request_date.day,
    )

    try:
        context = {}
        context['entry'] = entries.get(slug=entry_slug)
        return render(request, 'main/project_details.html', context)

    except ProjectEntry.DoesNotExist:
        raise Http404("No entry matches the given query.")


def about(request):
    return render(request, 'main/about.html')
