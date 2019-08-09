# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse
from datetime import date
from calendar import HTMLCalendar, month_name
from django.http import HttpResponseRedirect
from .forms import VenueForm
# Create your views here.

month_dictionary = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May",
                    6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep",  10: "Oct", 11: "Nov", 12: "Dec"}


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def default_home(request):
    day_variable = date.today()
    month = date.strftime(day_variable, '%b')
    year = day_variable.year
    page_title = f"Events Notifier - {month},{year}"
    calender_html = HTMLCalendar().formatmonth(year, day_variable.month)
    # return HttpResponse(f"<h2>{page_title}</h2><p>{calender_html}</p>")
    current_month = date.today().month
    month_list = [{current_month + x + 1: month_dictionary[current_month + x + 1]}
                  for x in range(12 - current_month)]
    return render(request, 'events/calender_base.html', {'page_title': page_title, 'calender_html': calender_html, 'month': month_list, 'year': year})


def sepcified_date(request, year, month_number):
    month = month_name[int(month_number)]
    page_title = f'Events Notifier - {month[0:3]},{year}'
    calender_html = HTMLCalendar().formatmonth(int(year), int(month_number))
    month_list = [{int(month_number) + x + 1: month_dictionary[int(month_number) + x + 1]}
                  for x in range(12 - int(month_number))]
    # return HttpResponse(f"<h2>{page_title}</h2><p>{calender_html}</p>")
    return render(request, 'events/calender_base.html', {'page_title': page_title, 'calender_html': calender_html, 'month': month_list, 'year': year})
