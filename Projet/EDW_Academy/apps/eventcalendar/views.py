from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Module, Camp, Course


def calendarView(request):
    context = {'camps': Camp.objects.all(), 'modules': Module.objects.all(), 'courses': Course.objects.all()}
    return render(request, 'myaccount.html', context)
