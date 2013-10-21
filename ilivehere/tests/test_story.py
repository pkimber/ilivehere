from django.test import TestCase

from ilivehere.tests.model_maker import (
    make_story,
)
from ilivehere.tests.scenario import (
    default_scenario_ilivehere,
    get_area_hatherleigh,
    get_story_craft_fair,
)
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    user_contractor,
)


class TestStory(TestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_ilivehere()

    def test_create_anon(self):
        make_story(
            name='Pat',
            email='code@pkimber.net',
            area=get_area_hatherleigh(),
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def test_create_trust(self):
        make_story(
            user=get_user_staff(),
            area=get_area_hatherleigh(),
            title='10 Pub Barrel Pull Success',
            description='10 Pub Pull on Saturday',
        )

    def test_create_no_user_or_name(self):
        self.assertRaises(
            ValueError,
            make_story,
            area=get_area_hatherleigh(),
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def test_set_moderated(self):
        story = get_story_craft_fair()
        story.set_moderated(get_user_staff())
        story.save()
        self.assertTrue(get_story_craft_fair().moderated)
