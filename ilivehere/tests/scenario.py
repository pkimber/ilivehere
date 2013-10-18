from ilivehere.models import (
    Area,
    Story,
)
from ilivehere.tests.model_maker import (
    make_area,
    make_story,
)
from login.tests.scenario import (
    get_user_staff,
)


def get_area_exbourne():
    return Area.objects.get(name='Exbourne')


def get_area_hatherleigh():
    return Area.objects.get(name='Hatherleigh')


def get_story_craft_fair():
    return Story.objects.get(title='Craft Fair')


def default_scenario_ilivehere():
    make_area('Hatherleigh')
    make_area('Exbourne')
    make_story(
        user=get_user_staff(),
        area=get_area_hatherleigh(),
        title='MGs descend on Hatherleigh',
        description=(
            "The Taw and Torridge MG owners club came to Hatherleigh, on "
            "Tuesday, to join the crowds at Hatherleigh Market. They came "
            "to visit Martin at the Hatherleigh Fish Bar. Martin the owner "
            "of the bar also has two MGs."
        )
    )
    make_story(
        name='Pat',
        email='code@pkimber.net',
        area=get_area_exbourne(),
        title='Craft Fair',
        description=(
            "Over 200 entries were exhibited at the Hatherleigh Craft Show, "
            "at its launch in Hatherleigh Community Centre on Sunday 4th "
            "August. Judges had the difficult task of awarding rosettes for "
            "1st, 2nd & 3rd places in each of the 24 classes, ranging from "
            "knitting to metal work."
        )
    )
