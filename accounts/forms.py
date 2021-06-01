from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=20, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone Number', max_length=20, min_length=5,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    voter_id = forms.CharField(label='Voter ID', max_length=20, min_length=5,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    place = forms.CharField(label='Block / Constituency', max_length=20, min_length=5,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    CHOICES = [('M','Male'),('F','Female')]
    Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
