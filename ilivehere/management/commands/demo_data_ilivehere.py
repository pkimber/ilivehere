from django.core.management.base import BaseCommand

from ilivehere.tests.scenario import default_scenario_ilivehere


class Command(BaseCommand):

    help = "Create demo data for 'ilivehere'"

    def handle(self, *args, **options):
        default_scenario_ilivehere()
        print("Created 'ilivehere' demo data...")
