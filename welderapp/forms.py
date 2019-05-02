from django import forms
from weldingapp . models import Order, Item
from .models import Design,User


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('client_name', 'date_of_order', 'date_of_completion', 'cover')

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'length_feet', 'height_feet', 'cost', 'design')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ItemUpdateForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'length_feet', 'height_feet', 'cost', 'design')



class DesignForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = ('design_name', 'desc', 'cost', 'picture')



