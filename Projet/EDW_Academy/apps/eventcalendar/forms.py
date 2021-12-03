from django import forms
from apps import userprofile
from .models import Course, Camp


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'start_time', 'end_time', 'date']
        labels = {'title': 'Title', 'description': 'Description', 'start_time': 'Start time', 'end_time': 'End time',
                  'date': 'Date'}


class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['title', 'description', 'start_date', 'end_date', 'game', 'nb_places', 'nb_registered']
        labels = {'title': 'Title', 'description': 'Description', 'start_date': 'Start date',
                  'end_date': 'End date', 'game': 'Game', 'nb_places': 'Nb_places', 'nb_registered': 'Nb_registered'}


