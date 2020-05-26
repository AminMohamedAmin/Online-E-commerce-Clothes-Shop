from django import forms
from .models import order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ('first_name','last_name','email','address','postal_code','city','mobile')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', }),
            'city': forms.TextInput(attrs={'class': 'form-control', }),
            'mobile': forms.TextInput(attrs={'class': 'form-control', }),
        }