from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


QUANTITY_CHOICES = (
    (0, _('0 cl')),
    (2, _('2 cl')),
    (4, _('4 cl')),
    (6, _('6 cl')),
    (8, _('8 cl')),
    (10, _('10 cl')),
    (12, _('12 cl')),
    (14, _('14 cl')),
    (16, _('16 cl')),
    (18, _('18 cl')),
    (20, _('20 cl')),
    (22, _('22 cl')),
    (24, _('24 cl'))
)


class IDField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('primary_key', True)
        kwargs['default'] = kwargs.get('default', uuid4)
        kwargs['editable'] = False
        kwargs['verbose_name'] = kwargs.get('verbose_name', _('ID'))
        super().__init__(*args, **kwargs)


class Person(models.Model):
    id = IDField()

    first_name = models.CharField(max_length=256, verbose_name=_('first name'))
    last_name = models.CharField(max_length=256, verbose_name=_('last name'))
    nickname = models.CharField(max_length=256, blank=True, verbose_name=_('nickname'))

    class Meta:
        ordering = ('first_name', 'last_name', 'nickname')
        verbose_name = _('person')
        verbose_name_plural = _('people')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} "{self.nickname}" {self.last_name}' if self.nickname else f'{self.first_name} {self.last_name}'

    @property
    def short_name(self):
        return self.nickname or f'{self.first_name} {self.last_name[0]}'


class Consumption(models.Model):
    id = IDField()

    timestamp = models.DateTimeField(default=now, editable=False, verbose_name=_('timestamp'))

    person = models.ForeignKey(Person, verbose_name=_('person'))
    quantity = models.PositiveIntegerField(choices=QUANTITY_CHOICES, default=0, verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('consumption')
        verbose_name_plural = _('consumptions')

    def __str__(self):
        return f'{self.person.short_name}: {self.quantity} cl ({self.timestamp})'


class User(AbstractUser):
    id = IDField()
