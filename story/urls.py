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
    url(regex=r'^story/create/anon/$',
        view=StoryAnonCreateView.as_view(),
        name='story.create.anon'
        ),
    url(regex=r'^story/create/trust/$',
        view=StoryTrustCreateView.as_view(),
        name='story.create.trust'
        ),
    url(regex=r'^story/(?P<pk>\d+)/$',
        view=StoryDetailView.as_view(),
        name='story.detail'
        ),
    url(regex=r'^story/$',
        view=StoryListView.as_view(),
        name='story.list'
        ),
    url(regex=r'^story/(?P<pk>\d+)/approve/$',
        view=StoryModerateView.as_view(),
        name='story.moderate'
        ),
    url(regex=r'^story/(?P<pk>\d+)/edit/$',
        view=StoryUpdateView.as_view(),
        name='story.update'
        ),
)
