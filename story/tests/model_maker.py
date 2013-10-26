from base.tests.model_maker import clean_and_save

from story.models import (
    Area,
    Story,
)


def make_area(name, **kwargs):
    return clean_and_save(
        Area(
            name=name,
            **kwargs
        )
    )


def make_story(**kwargs):
    return clean_and_save(
        Story(
            **kwargs
        )
    )
