from base.form_utils import (
    RequiredFieldForm,
)

from .models import Story


class StoryAnonForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(StoryAnonForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['name'].widget.attrs.update(
            {'class': 'pure-input-1-2'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'pure-input-1-2'}
        )
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = Story
        fields = ('name', 'email', 'area', 'title', 'description', 'picture')


class StoryTrustForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(StoryTrustForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = Story
        fields = ('area', 'title', 'description', 'picture')


class StoryUpdateForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(StoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = Story
        fields = ('moderated', 'area', 'title', 'description', 'picture')
