from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from braces.views import (
    LoginRequiredMixin,
)

from .forms import (
    StoryAnonForm,
    StoryTrustForm,
)
from .models import Story


class StoryAnonCreateView(CreateView):

    model = Story
    form_class = StoryAnonForm


class StoryTrustCreateView(LoginRequiredMixin, CreateView):

    model = Story
    form_class = StoryTrustForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(StoryTrustCreateView, self).form_valid(form)


class StoryDetailView(DetailView):
    model = Story


class StoryListView(ListView):
    model = Story
