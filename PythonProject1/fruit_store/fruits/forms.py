from django import forms
from .models import Fruit


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'description', 'price']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'uk-input',
                'placeholder': 'Яблоки, Апельсины...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'uk-textarea',
                'rows': 3,
                'placeholder': 'Сорт, страна происхождения...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'uk-input',
                'step': '0.01',
                'min': '0'
            })
        }