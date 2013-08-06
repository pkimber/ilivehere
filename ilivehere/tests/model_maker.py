from base.tests.model_maker import clean_and_save

from ilivehere.models import Area


def make_area(name, **kwargs):
    return clean_and_save(
        Area(
            name=name,
            **kwargs
        )
    )
