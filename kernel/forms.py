from django.forms import ModelForm
from kernel.models import Comment

__author__ = 'sherlock'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['com_user', 'com_mail', 'com_data']
