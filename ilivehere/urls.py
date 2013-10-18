from django.conf.urls import (
    patterns, url
)

from .views import (
    StoryAnonCreateView,
    StoryDetailView,
    StoryListView,
    StoryTrustCreateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^story/anon/add/$',
        view=StoryAnonCreateView.as_view(),
        name='ilivehere.story.anon.create'
        ),
    url(regex=r'^story/trust/add/$',
        view=StoryTrustCreateView.as_view(),
        name='ilivehere.story.trust.create'
        ),
    url(regex=r'^story/(?P<pk>\d+)/$',
        view=StoryDetailView.as_view(),
        name='ilivehere.story.detail'
        ),
    url(regex=r'^story/$',
        view=StoryListView.as_view(),
        name='ilivehere.story.list'
        ),
)
