from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Block(models.Model):
    name = models.CharField(
        max_length=10,
        null=False,
        unique=True
    )
    slug = models.SlugField(
        help_text="leave this field blank",
        unique=True,
        null=True,
        blank=True
    )
    total_rooms = models.IntegerField(
        null=False
    )
    remaining_rooms = models.IntegerField(
        default=None,
        help_text="leave this field blank"
    )
    timestamp = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    # def get_absolute_url(self):
    #     return reverse('accomodation-app:hostel-detail-view', kwargs=({'name': self.name}))

    def __str__(self):
        return self.name
