from django import forms
from .models import StockTickers

class StockForm(forms.ModelForm):
    class Meta:
        model = StockTickers
        fields = ['ticker']
