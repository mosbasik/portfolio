# django imports
from django.http import Http404
from django.shortcuts import render

# local imports
from main.models import Entry

# python imports
from datetime import datetime
import pytz


def home(request):
    return render(request, 'main/home.html')


def blog_list(request):
    context = {}
    context['entries'] = Entry.objects.filter(kind='Blog').order_by('-display_date')
    return render(request, 'main/blog_list.html', context)


def blog_details(request, year, month, day, entry_slug):
    request_date = datetime(int(year), int(month), int(day))
    entries = Entry.objects.filter(
        created__year=request_date.year,
        created__month=request_date.month,
        created__day=request_date.day,
    )

    try:
        context = {}
        context['entry'] = entries.get(slug=entry_slug)
        return render(request, 'main/blog_details.html', context)

    except Entry.DoesNotExist:
        raise Http404("No entry matches the given query.")
