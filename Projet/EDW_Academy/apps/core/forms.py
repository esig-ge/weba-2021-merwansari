from django import forms

from apps.eventcalendar.models import Module


class FormGameLOL(forms.Form):
    ModuleListLOL = forms.ModelChoiceField(queryset=Module.objects.filter(game__abbreviation="LOL"), required=False, label='')


class FormGameRL(forms.Form):
    ModuleListRL = forms.ModelChoiceField(queryset=Module.objects.filter(game__abbreviation="RL"), required=False, label='')


class FormGameTM(forms.Form):
    ModuleListTM = forms.ModelChoiceField(queryset=Module.objects.filter(game__abbreviation="TM"), required=False, label='')


class FormGameVALO(forms.Form):
    ModuleListVALO = forms.ModelChoiceField(queryset=Module.objects.filter(game__abbreviation="VALO"), required=False, label='')


class FormGameSSBU(forms.Form):
    ModuleListSSBU = forms.ModelChoiceField(queryset=Module.objects.filter(game__abbreviation="SSBU"), required=False, label='')


class FormGameHS(forms.Form):
    ModuleListHS = forms.ModelChoiceField(queryset=Module.objects.filter(game__abbreviation="HS"), required=False, label='')