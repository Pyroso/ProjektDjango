from django import forms
from aplikacja.models import Notatka

class NotatkaForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ('title', 'body','author','status')
        widgets = {
            'body': forms.Textarea(attrs={'rows': 10, 'cols': 40})
        }
