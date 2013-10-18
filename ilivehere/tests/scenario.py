from ilivehere.models import Area
from ilivehere.tests.model_maker import make_area


def default_scenario_ilivehere():
    make_area('Hatherleigh')
    make_area('Exbourne')


def get_area_hatherleigh():
    return Area.objects.get(name='Hatherleigh')
