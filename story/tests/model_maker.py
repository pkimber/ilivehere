from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from story.models import (
    Area,
    Story,
)


def make_area(name, **kwargs):
    defaults = dict(
        name=name,
        slug=slugify(unicode(name)),
    )
    defaults.update(kwargs)
    return clean_and_save(Area(**defaults))


def make_story(**kwargs):
    return clean_and_save(
        Story(
            **kwargs
        )
    )
