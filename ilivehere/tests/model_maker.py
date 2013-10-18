from base.tests.model_maker import clean_and_save

from ilivehere.models import (
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


def make_story_anon(name, email, area, title, description, **kwargs):
    """'name' and 'email' for story created by an anonymous user"""
    return clean_and_save(
        Story(
            name=name,
            email=email,
            area=area,
            title=title,
            description=description,
            **kwargs
        )
    )


def make_story_trust(user, area, title, description, **kwargs):
    """'user' for story created by a trusted user"""
    return clean_and_save(
        Story(
            user=user,
            area=area,
            title=title,
            description=description,
            **kwargs
        )
    )
