from django import forms
from vins.models import Vin
from vins.humanize import naturalsize
from django.core.exceptions import ValidationError
from django.core import validators


# Form Comment
class CommentForm(forms.Form):
    comment = forms.CharField(
        required=True,
        max_length=141,
        min_length=1,
        strip=True)
