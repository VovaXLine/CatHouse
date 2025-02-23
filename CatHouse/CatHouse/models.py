from django.db import models
from django.utils.translation import gettext_lazy as _

class Volunteer(models.Model):
    name = models.CharField(_('Имя'), max_length=100)
    age = models.IntegerField(_('Возраст'))
    city = models.CharField(_('Город'), max_length=100)
    type_of_activity = models.CharField(_('Род деятельности'), max_length=100)

    def __str__(self):
        return self.name