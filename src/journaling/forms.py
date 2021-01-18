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
    # gratefulOf = forms.TextField(
    #     label='What am I grateful of today?',
    #     required=True
    #     )
    # please don't forget about this
    class Meta:
        model = GratefulFor
        fields = "__all__"
        # fields = [
        #     'user',
        #     'grategulOf'
        # ]

class SmallVictoryForm(forms.ModelForm):
    # user = forms.CharField(
    #     label='Your name',
    #     widget=forms.TextInput(
    #     attrs = {
    #         'placeholder':'your Name'
    #         }
    #     )
    # )
    # dailyVictory = forms.TextField(
    #     label='What small or big thing led me closer to my goal?',
    #     required=True
    #     )
    class Meta:
        model = SmallVictory
        fields = "__all__"
        # fields = [
        #     'user',
        #     'dailyVictory'
        # ]