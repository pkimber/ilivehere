from django.forms import ModelForm

from .models import Story


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ("name", "email", "area", "title", "description", )
