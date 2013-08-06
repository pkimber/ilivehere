from django.views.generic import CreateView

from .models import Story


class StoryCreateView(CreateView):
    model = Story
