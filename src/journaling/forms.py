from django import forms
from .models import (
    GratefulFor,
    SmallVictory
    )

class GratefulForForm(forms.ModelForm):
    user = forms.CharField(
        label='Your name',
        widget=forms.TextInput(
        attrs = {
            'placeholder':'your Name'
            }
        )
    )
    gratefulOf = forms.CharField(
        label='What am I grateful of today?',
        required=True
        )

class SmallVictoryForm(forms.ModelForm):
    user = forms.CharField(
        label='Your name',
        widget=forms.TextInput(
        attrs = {
            'placeholder':'your Name'
            }
        )
    )
    dailyVictory = forms.CharField(
        label='What small or big thing led me closer to my goal?',
        required=True
        )