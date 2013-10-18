from django.core.urlresolvers import reverse
from django.test import TestCase

from ilivehere.models import Story
from ilivehere.tests.model_maker import (
    make_area,
    make_story_anon,
    make_story_trust,
)


class TestStory(TestCase):

    def test_create_anon(self):
        pass
