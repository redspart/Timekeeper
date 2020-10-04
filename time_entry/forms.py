from django import forms
from .models import TimeEntry

class TimeEntryCreate(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = "__all__"