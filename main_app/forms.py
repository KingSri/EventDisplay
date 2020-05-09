from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields = ('title', 'description', 'start_time', 'likes')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
