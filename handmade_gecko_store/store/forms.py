from django import forms
from .models import Products, UserProfile, Orders, Custom_orders, Roles

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products

        fields = [
            'name',
            'amount_left',
            'price',
            'in_stock',
            'leather_type',
            'image',
            'image2',
            'image3',
        ]

class RegisterForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField()
    preferred_contact = forms.ChoiceField(choices=UserProfile.preferred_contact_way)