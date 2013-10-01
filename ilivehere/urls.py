from django.conf.urls import (
    patterns, url
)

from .views import (
    StoryCreateView,
    StoryDetailView,
    StoryListView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^story/add/$',
        view=StoryCreateView.as_view(),
        name='ilivehere.story.create'
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
