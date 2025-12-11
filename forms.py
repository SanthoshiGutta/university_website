from django import forms
from .models import Admin

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=['name','father_name','gender','hall_ticket_number','branch','college']