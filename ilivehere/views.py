from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from .forms import (
    StoryAnonForm,
    StoryTrustForm,
    StoryUpdateForm,
)
from .models import Story
from base.view_utils import BaseMixin


class StoryAnonCreateView(BaseMixin, CreateView):

    model = Story
    form_class = StoryAnonForm
    template_name = 'ilivehere/story_create_form.html'


class StoryTrustCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'ilivehere/story_create_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(StoryTrustCreateView, self).form_valid(form)


class StoryDetailView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, DetailView):
    model = Story


class StoryListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = Story


class StoryUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    model = Story
    form_class = StoryUpdateForm
    template_name = 'ilivehere/story_update_form.html'
