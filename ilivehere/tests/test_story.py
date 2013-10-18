from django.test import TestCase

from ilivehere.tests.model_maker import (
    make_story_anon,
    make_story_trust,
)
from ilivehere.tests.scenario import (
    default_scenario_ilivehere,
    get_area_hatherleigh,
)
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
)


class TestStory(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_ilivehere()

    def test_create_anon(self):
        make_story_anon(
            name='Pat',
            email='code@pkimber.net',
            area=get_area_hatherleigh(),
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def test_create_trust(self):
        make_story_trust(
            user=get_user_staff(),
            area=get_area_hatherleigh(),
            title='10 Pub Barrel Pull Success',
            description='10 Pub Pull on Saturday',
        )
