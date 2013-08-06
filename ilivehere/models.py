from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

import reversion


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Area(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __unicode__(self):
        return unicode('{}'.format(self.name))

reversion.register(Area)


class Event(TimeStampedModel):
    """ Event """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.ForeignKey(Area)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    moderated = models.BooleanField(default=False)

    class Meta:
        ordering = ['modified']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __unicode__(self):
        return unicode('{}'.format(self.title))

reversion.register(Event)


class Story(TimeStampedModel):
    """ News story """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.ForeignKey(Area)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    moderated = models.BooleanField(default=False)

    class Meta:
        ordering = ['modified']
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __unicode__(self):
        return unicode('{}'.format(self.title))

    def get_absolute_url(self):
        return reverse('ilivehere.story.detail', args=[self.pk])

reversion.register(Story)
