from django import forms
from .models import DuoReg


class DuoForm(forms.ModelForm):
    class Meta:
        model = DuoReg
        fields = ('user', 'password',)