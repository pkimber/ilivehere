from django.test import TestCase

from ilivehere.tests.model_maker import (
    make_story,
)
from ilivehere.tests.scenario import (
    default_scenario_ilivehere,
    get_area_hatherleigh,
    get_story_craft_fair,
    get_story_market_fire,
)
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
    user_contractor,
)


class TestStory(TestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_ilivehere()

    def test_can_edit(self):
        """
        A story can be edited by the person who created it (or a member of
        staff).
        """
        story = get_story_market_fire()
        self.assertTrue(story.user_can_edit(get_user_web()))

    def test_can_edit_not(self):
        """
        A story can only be edited by the person who created it (or a member
        of staff).  The craft fair story was created by an anonymous user.
        """
        story = get_story_craft_fair()
        self.assertFalse(story.user_can_edit(get_user_web()))

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
