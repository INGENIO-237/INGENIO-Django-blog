from dataclasses import fields
from django.forms import ModelForm

from .models import Comment, CommentResponse

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CommentResponseForm(ModelForm):
    class Meta:
        model = CommentResponse
        fields = ['body']