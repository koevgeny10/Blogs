from django import forms
from . import models


class AvatarsForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['avatar']
