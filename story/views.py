from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from .forms import (
    StoryAnonForm,
    StoryEmptyForm,
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
    template_name = 'story/story_create_form.html'

    def get(self, request, *args, **kwargs):
        """
        If a user is logged in (and active), they shouldn't be using this
        view... they can use the view for a logged in user.
        """
        if self.request.user and self.request.user.is_active:
            return HttpResponseRedirect(reverse('story.create.trust'))
        else:
            return super(StoryAnonCreateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project.home')


class StoryTrustCreateView(
        LoginRequiredMixin, BaseMixin, CreateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'story/story_create_form.html'

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

    def get_success_url(self):
        return reverse('story.list')


class StoryDetailView(
        LoginRequiredMixin, CheckPermMixin, BaseMixin, DetailView):

    model = Story

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        self._check_perm(self.object)
        context.update(dict(
            user_can_edit=self.object.user_can_edit(self.request.user),
        ))
        return context


class StoryListView(
        LoginRequiredMixin, BaseMixin, ListView):

    def get_queryset(self):
        if self.request.user.is_staff:
            result = Story.objects.all()
        else:
            result = Story.objects.filter(user=self.request.user)
        return result


class StoryPublishView(
        LoginRequiredMixin, BaseMixin, UpdateView):

    model = Story
    form_class = StoryEmptyForm
    template_name = 'story/story_publish_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_published(self.request.user)
        messages.info(
            self.request,
            "Published story {}, {}".format(
                self.object.pk,
                self.object.title,
            )
        )
        return super(StoryPublishView, self).form_valid(form)

    def get_success_url(self):
        return reverse('story.list')


class StoryRejectView(
        LoginRequiredMixin, BaseMixin, UpdateView):

    model = Story
    form_class = StoryEmptyForm
    template_name = 'story/story_reject_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_rejected(self.request.user)
        messages.info(
            self.request,
            "Rejected story {}, {}".format(
                self.object.pk,
                self.object.title,
            )
        )
        return super(StoryRejectView, self).form_valid(form)

    def get_success_url(self):
        return reverse('story.list')


class StoryUpdateView(
        LoginRequiredMixin, CheckPermMixin, BaseMixin, UpdateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'story/story_update_form.html'

    def get_object(self, *args, **kwargs):
        obj = super(StoryUpdateView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        if not obj.user_can_edit(self.request.user):
            raise PermissionDenied()
        return obj
