from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Notatka(models.Model):
    Signiface = (
        ('mniejwazne', 'Mniejwazne'),
        ('wazne','Wazne')
    )
    STATUS_CHOICES = (
        ('mniejwazne', 'Mniejwazne'),
        ('wazne', 'Wazne')
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='notatki')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='mniejwazne')
    def get_absolute_url(self):
        return reverse("aplikacja:note_detail",
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                            ])

class Meta:
    ordering = ('-publish',)


def __str__(self):
    return self.title
