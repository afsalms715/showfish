from django import forms

from bookapp.models import bookShop


class bookform(forms.ModelForm):
    class Meta:
        model=bookShop
        fields="__all__"