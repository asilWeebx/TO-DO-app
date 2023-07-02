from datetime import timezone, datetime

from django.db import models

# from users.models import User


# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Topshiriq nomi', max_length=500)
    is_complete = models.BooleanField('Yakunlandi', default=False)
    info = models.TextField()
    bowlaniwi = models.DateTimeField(auto_now_add=True)
    yakunlaniwi = models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'Topshiriq'
        verbose_name_plural = 'Topshiriq'

    def __str__(self):
        return self.title, self.bowlaniwi

