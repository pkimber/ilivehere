from django.core.urlresolvers import reverse
from django.test import TestCase

from ilivehere.models import Story
from ilivehere.tests.scenario import (
    default_scenario_ilivehere,
    get_area_hatherleigh,
)


class TestViewStory(TestCase):

    def test_create_anon_get(self):
        url = reverse('ilivehere.story.create.anon')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_anon_post(self):
        default_scenario_ilivehere()
        url = reverse('ilivehere.story.create.anon')
        data = dict(
            name='Patrick',
            email='code@pkimber.net',
            area=get_area_hatherleigh().pk,
            title='Chilli Night',
            description='Hot, hot, hot...',
        )
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        Story.objects.get(name='Patrick')
