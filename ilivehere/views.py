from django.contrib import messages
from django.core.exceptions import PermissionDenied
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


def check_perm(user, story):
    """user must be a member of staff or have created the story"""
    if user.is_staff:
        pass
    elif not story.user == user:
        # the user did not create the story
        raise PermissionDenied()


class CheckPermMixin(object):

    def _check_perm(self, story):
        check_perm(self.request.user, story)


class StoryAnonCreateView(BaseMixin, CreateView):

    model = Story
    form_class = StoryAnonForm
    template_name = 'ilivehere/story_create_form.html'

    def get_context_data(self, **kwargs):
        """
        If a user is logged in (and active), they shouldn't be using this
        view!
        We don't do anything with the context... but it is a good place to
        check some stuff.
        """
        context = super(StoryAnonCreateView, self).get_context_data(**kwargs)
        if self.request.user and self.request.user.is_active:
            raise PermissionDenied()
        return context


class StoryTrustCreateView(
        LoginRequiredMixin, BaseMixin, CreateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'ilivehere/story_create_form.html'

    def get_context_data(self, **kwargs):
        """
        This view is for users who are logged in and active.
        We don't do anything with the context... but it is a good place to
        check some stuff.
        """
        context = super(StoryTrustCreateView, self).get_context_data(**kwargs)
        if not self.request.user and self.request.user.is_active:
            raise PermissionDenied()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(StoryTrustCreateView, self).form_valid(form)


class StoryDetailView(
        LoginRequiredMixin, CheckPermMixin, BaseMixin, DetailView):

    model = Story

    def get_object(self, *args, **kwargs):
        obj = super(StoryDetailView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        return obj


class StoryListView(
        LoginRequiredMixin, BaseMixin, ListView):

    def get_queryset(self):
        if self.request.user.is_staff:
            result = Story.objects.all()
        else:
            result = Story.objects.filter(user=self.request.user)
        return result


class StoryModerateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, DeleteView):
    """
    TODO should this be an update view with an empty form?  Might be safer
    than using a delete view
    """

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
        LoginRequiredMixin, CheckPermMixin, BaseMixin, UpdateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'ilivehere/story_update_form.html'

    def get_object(self, *args, **kwargs):
        obj = super(StoryUpdateView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        return obj
