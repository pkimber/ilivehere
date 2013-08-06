from django.conf.urls import (
    patterns, url
)

from .views import StoryCreateView


urlpatterns = patterns(
    '',
    url(regex=r'^story/add/$',
        view=StoryCreateView.as_view(),
        name='ilivehere.story'
        ),
)
