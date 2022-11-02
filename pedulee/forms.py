from django import forms
from .models import Cloth, Groceries, Profile, Volunteer, Money, Groceries
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'birthdate', 'address')

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ['cloth_model', 'material', 'type']

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['name', 'email', 'pnumber', 'donation', 'message', 'ccnumber']


class VolunteerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control col'
    class Meta:
        model = Volunteer
        fields = ['project', 'divisi']

class GroceriesForm(forms.ModelForm):
    class Meta:
        model = Groceries
        fields = ['donasi', 'sembako', 'amount', 'pmethod', 'ccnumber']