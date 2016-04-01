from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Author(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    isbn = models.CharField(_('ISBN'), max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.name
