from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
# from django.contrib.auth.models import User
from home.models import Users

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('email','username', 'first_name', 'last_name','phone_number','birth_date','ngaylapthe','ngayhethan')
      

class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)