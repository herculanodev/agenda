from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_event = models.DateTimeField(verbose_name= 'data do evento')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'evento'
