from django import forms
from weldingapp. models import Item
from .models import Design, User , Demand


class OrderForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ('name', 'date_of_order','cover')

class DesignForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = ('item', 'length_feet', 'height_feet', 'cost', 'design')

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item', 'length_feet', 'height_feet', 'cost', 'design')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ItemUpdateForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = ('item', 'length_feet', 'height_feet', 'cost', 'design')





