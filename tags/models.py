from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):

    class TagColor(models.TextChoices):
        BLACK = 'black', _('Black')
        DARK = 'dark', _('Dark')
        LIGHT = 'light', _('Light')
        WHITE = 'white', _('White')
        PRIMARY = 'primary', _('Primary')
        LINK = 'link', _('Link')
        INFO = 'info', _('Info')
        SUCCESS = 'success', _('Success')
        WARNING = 'warning', _('Warning')
        DANGER = 'danger', _('Danger')

    name = models.CharField(unique=True, max_length=128)
    color = models.CharField(max_length=10, choices=TagColor.choices, default=TagColor.PRIMARY)

    def __str__(self):
        return self.name

    def get_bulma_color_class(self):
        return f'is-{self.color}'
