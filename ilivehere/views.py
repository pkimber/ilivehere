from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
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


class StoryModerateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, DeleteView):

    model = Story

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.set_moderated(self.request.user)
        self.object.save()
        messages.info(
            self.request,
            "Published story {}, {}".format(
                self.object.pk,
                self.object.title,
            )
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()


class StoryUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'ilivehere/story_update_form.html'
