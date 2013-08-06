from django.forms import ModelForm

from .models import Story


class StoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'pure-input-1-2'})
        self.fields['email'].widget.attrs.update({'class': 'pure-input-1-2'})
        self.fields['title'].widget.attrs.update({'class': 'pure-input-2-3'})
        self.fields['description'].widget.attrs.update({'class': 'pure-input-2-3'})

    class Meta:
        model = Story
        fields = ("name", "email", "area", "title", "description", )
