from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Initialise 'ilivehere' application"

    def handle(self, *args, **options):
        print "Initialised 'ilivehere' app..."
