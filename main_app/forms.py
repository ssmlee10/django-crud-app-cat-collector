from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
    # don't add cats because we don't want to display that to the user
    widgets = {
      'date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          'placeholder': 'Select a date',
          'type': 'date'
        }
      )
    }