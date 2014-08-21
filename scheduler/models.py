from django.db import models

class Schedule(models.Model):
    event_date = models.DateField()

