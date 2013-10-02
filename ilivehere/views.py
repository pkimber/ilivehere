from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from braces.views import (
    LoginRequiredMixin,
)

from .forms import StoryForm
from .models import Story


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    form_class = StoryForm


class StoryDetailView(DetailView):
    model = Story


class StoryListView(ListView):
    model = Story
