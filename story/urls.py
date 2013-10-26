from django.conf.urls import (
    patterns, url
)

from .views import (
    StoryAnonCreateView,
    StoryDetailView,
    StoryListView,
    StoryModerateView,
    StoryTrustCreateView,
    StoryUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^create/anon/$',
        view=StoryAnonCreateView.as_view(),
        name='story.create.anon'
        ),
    url(regex=r'^create/trust/$',
        view=StoryTrustCreateView.as_view(),
        name='story.create.trust'
        ),
    url(regex=r'^(?P<pk>\d+)/$',
        view=StoryDetailView.as_view(),
        name='story.detail'
        ),
    url(regex=r'^$',
        view=StoryListView.as_view(),
        name='story.list'
        ),
    url(regex=r'^(?P<pk>\d+)/approve/$',
        view=StoryModerateView.as_view(),
        name='story.moderate'
        ),
    url(regex=r'^(?P<pk>\d+)/edit/$',
        view=StoryUpdateView.as_view(),
        name='story.update'
        ),
)
