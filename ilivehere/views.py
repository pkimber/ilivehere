from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView
)

from braces.views import (
    LoginRequiredMixin,
)

from .forms import (
    StoryAnonForm,
    StoryTrustForm,
    StoryUpdateForm,
)
from .models import Story


class StoryAnonCreateView(CreateView):

    model = Story
    form_class = StoryAnonForm
    template_name = 'ilivehere/story_create_form.html'


class StoryTrustCreateView(LoginRequiredMixin, CreateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'ilivehere/story_create_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(StoryTrustCreateView, self).form_valid(form)


class StoryDetailView(DetailView):
    model = Story


class StoryListView(LoginRequiredMixin, ListView):
    model = Story


class StoryUpdateView(LoginRequiredMixin, UpdateView):

    model = Story
    form_class = StoryUpdateForm
    template_name = 'ilivehere/story_update_form.html'
