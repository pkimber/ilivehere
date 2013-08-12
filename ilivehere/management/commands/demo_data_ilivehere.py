from django.core.management.base import BaseCommand

from ilivehere.tests.model_maker import make_area


class Command(BaseCommand):

    help = "Create demo data for 'ilivehere'"

    def handle(self, *args, **options):
        make_area('Hatherleigh')
        make_area('Exbourne')
        print("Created 'ilivehere' demo data...")
