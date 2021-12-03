from django.db import models


class Game(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    NOT_OPEN = 'New'
    Pending = 'In progress'
    Completed = 'Completed'
    STATUT_TICKET = (
        (NOT_OPEN, 'New'),
        (Pending,'Pending'),
        (Completed, 'Completed'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    status = models.CharField(max_length=20, choices=STATUT_TICKET, default=NOT_OPEN)

    def __str__(self):
        return self.name