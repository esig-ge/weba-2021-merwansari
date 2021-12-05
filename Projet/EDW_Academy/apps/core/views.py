from django.core.mail import send_mail
from django.shortcuts import render, redirect

from EDW_Academy import settings
from apps.core import forms
from apps.eventcalendar.models import Camp, Module
from apps.core.models import Game, Ticket
from django.http import JsonResponse
from apps.reservation.views import createModule


def ticket(request):
    if request.method == "POST":
        ticket = Ticket()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('Subject')
        ticket.name = name
        ticket.email = email
        ticket.subject = subject
        ticket.save()
        return redirect(home)
    return render(request, 'ticket.html')


def home(request):
    return render(request, 'home.html')


def camps(request):
    return render(request, 'camps.html')


def games(request):
    return render(request, 'games.html')


def courses(request):
    moduleLOL = Module.objects.filter(game__abbreviation="LOL")
    moduleRL = Module.objects.filter(game__abbreviation="RL")
    moduleTM = Module.objects.filter(game__abbreviation="TM")
    moduleVALO = Module.objects.filter(game__abbreviation="VALO")
    moduleSSBU = Module.objects.filter(game__abbreviation="SSBU")
    moduleHS = Module.objects.filter(game__abbreviation="HS")
    formLOL1 = forms.FormGameLOL()
    formRL1 = forms.FormGameRL()
    formTM1 = forms.FormGameTM()
    formVALO1 = forms.FormGameVALO()
    formSSBU1 = forms.FormGameSSBU()
    formHS1 = forms.FormGameHS()
    if request.method == 'POST':
        if 'boutonLOL' in request.POST:
            formLOL1 = forms.FormGameLOL(request.POST)
            if formLOL1.is_valid():
                answer = formLOL1.cleaned_data['ModuleListLOL']
                createModule(request, answer)

        if 'boutonRL' in request.POST:
            formRL1 = forms.FormGameRL(request.POST)
            if formRL1.is_valid():
                answer = formRL1.cleaned_data['ModuleListRL']
                createModule(request, answer)
        if 'boutonTM' in request.POST:
            formTM1 = forms.FormGameTM(request.POST)
            if formTM1.is_valid():
                answer = formTM1.cleaned_data['ModuleListTM']
                createModule(request, answer)
        if 'boutonVALO' in request.POST:
            formVALO1 = forms.FormGameVALO(request.POST)
            if formVALO1.is_valid():
                answer = formVALO1.cleaned_data['ModuleListVALO']
                createModule(request, answer)
        if 'boutonSSBU' in request.POST:
            formSSBU1 = forms.FormGameSSBU(request.POST)
            if formSSBU1.is_valid():
                answer = formSSBU1.cleaned_data['ModuleListSSBU']
                createModule(request, answer)
        if 'boutonHS' in request.POST:
            formHS1 = forms.FormGameHS(request.POST)
            if formHS1.is_valid():
                answer = formHS1.cleaned_data['ModuleListHS']
                createModule(request, answer)
    context = {'moduleLOL': moduleLOL,
               'moduleRL': moduleRL,
               'moduleTM': moduleTM,
               'moduleVALO': moduleVALO,
               'moduleSSBU': moduleSSBU,
               'moduleHS': moduleHS,
               'formLOL': formLOL1,
               'formRL': formRL1,
               'formTM': formTM1,
               'formVALO': formVALO1,
               'formSSBU': formSSBU1,
               'formHS': formHS1}
    return render(request, 'courses.html', context)


def discover_camp(request):
    context = {'camps': Camp.objects.all()}
    print(Camp.objects.all())

    return render(request, 'discover_camp.html', context)


def improve_camp(request):
    context = {'camps': Camp.objects.all(),
               'game': Game.objects.all()}
    return render(request, 'improve_camp.html', context)


def get_json_game_data(request):
    qs_val = list(Game.objects.values())
    return JsonResponse({'data': qs_val})


def get_json_camp_data(request, *args, **kwargs):
    selected_game = kwargs.get('game')
    obj_camps = list(Camp.objects.filter(game__name=selected_game).values())
    return JsonResponse({'data': obj_camps})
