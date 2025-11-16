from django import forms
from .models import Heading, TodoItem


class HeadingForm(forms.ModelForm):
    class Meta:
        model = Heading
        fields = ['title']


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['description']
