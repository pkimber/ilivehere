from django.core.urlresolvers import reverse
from django.test import TestCase

from ilivehere.models import Story
from ilivehere.tests.model_maker import make_area
from ilivehere.tests.scenario import default_scenario_ilivehere


class TestViewStory(TestCase):

    def test_create(self):
        default_scenario_ilivehere()
        area = make_area('Hatherleigh')
        url = reverse('ilivehere.story.anon.create')
        data = dict(
            name='Patrick',
            email='code@pkimber.net',
            area=area.pk,
            title='Chilli Night',
            description='Hot, hot, hot...',
        )
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        Story.objects.get(name='Patrick')
