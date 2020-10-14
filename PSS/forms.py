from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Hub, UserProfile, Load, Panel

AREA_CHOICES = [
   ('NSW','NSW'),
   ('QLD','Queensland'),
   ('WA','Western Aus'),
   ('SA', 'South Aus'),
   ('NT', 'Northern Territory'),
   ('VIC','Victoria')
]

LOAD_CHOICES = [
    ('LED lighting','LED lighting'),
    ('PC','PC'),
    ('Fridge','Fridge'),
    ('TV','TV')
]

BOOLEAN_CHOICES = ((True,'Yes'),(False,'No'))

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Username','id':'username'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Enter your Password', 'id':'password1'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Re-enter your Password','id':'password2'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your Email address'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
    # hubID = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Hub ID'}))
    area = forms.CharField(label='Chose your living area', widget=forms.Select(choices=AREA_CHOICES))

    class Meta:
        model = UserProfile
        fields = ['area']

class HubForm(ModelForm):
    class Meta:
        model = Hub
        fields = ['hub_name']


class LoadForm(ModelForm):
    load_name = forms.CharField(widget=forms.Select(choices = LOAD_CHOICES))
    essential = forms.ChoiceField(choices = BOOLEAN_CHOICES,
                                  label='Is your load essential? (cannot be situationally cut down)',
                                  widget=forms.Select())
    class Meta:
        model = Load
        fields = ['load_name', 'essential']


class PanelForm(ModelForm):
    class Meta:
        model = Panel
        fields = ['panel_name', 'rated_power']

