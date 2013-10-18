from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from base.model_utils import TimeStampedModel


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
    """News story"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.ForeignKey(Area)
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='story/%Y/%m/%d', blank=True)
    moderated = models.BooleanField(default=False)

    class Meta:
        ordering = ['modified']
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __unicode__(self):
        return unicode('{}'.format(self.title))

    def save(self, *args, **kwargs):
        if self.user:
            pass
        elif self.email and self.name:
            pass
        else:
            raise ValueError(
                "Story must have a 'user' or a 'name' AND 'email'"
            )
        super(Story, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ilivehere.story.detail', args=[self.pk])

reversion.register(Story)
