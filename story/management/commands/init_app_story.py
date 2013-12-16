from django.core.management.base import BaseCommand

from story.tests.scenario import create_default_moderate_state


class Command(BaseCommand):

    help = "Initialise 'story' application"

    def handle(self, *args, **options):
        create_default_moderate_state()
        print "Initialised 'story' app..."
