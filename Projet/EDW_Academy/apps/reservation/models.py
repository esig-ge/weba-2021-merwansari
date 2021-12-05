from django.db import models
from apps.core.models import Game
from apps.eventcalendar.models import Camp, Module
from apps.userprofile.models import User


class CampOrder(models.Model):
    pending = "Pending"
    completed = "Completed"

    CHOICE_STATUS = (
        (pending, 'Pending'),
        (completed, 'Completed'),
    )
    user = models.ForeignKey(User, related_name='CampOrders', on_delete=models.SET_NULL, blank=True, null=True)
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=CHOICE_STATUS, default=pending)

    def __str__(self):
        return str(self.pk)


class ModuleOrder(models.Model):
    pending = "Pending"
    completed = "Completed"

    CHOICE_STATUS = (
        (pending, 'Pending'),
        (completed, 'Completed'),
    )
    user = models.ForeignKey(User, related_name="ModuleOrders", on_delete=models.SET_NULL, blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=CHOICE_STATUS, default=pending)

    def __str__(self):
        return str(self.pk)