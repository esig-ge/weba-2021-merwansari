from django.db import models
from ..core.models import Game


class Camp(models.Model):
    CAMP_CHOICES = (
        ('Improve_camp', 'Improve camp'),
        ('Discover_camp', 'Discover camp'),
    )
    type = models.CharField(max_length=200, choices=CAMP_CHOICES, null=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    nb_places = models.IntegerField(default=12)
    nb_registered = models.IntegerField(default=0)
    price = models.FloatField()

    def __str__(self):
        return self.type


class Course(models.Model):
    WEEKDAYS_CHOICES = (
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    )
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course_days = models.CharField(max_length=10, choices=WEEKDAYS_CHOICES)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ManyToManyField(Course)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.FloatField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
