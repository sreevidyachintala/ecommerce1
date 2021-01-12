from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Usreg(UserCreationForm):
	password1= forms.CharField(widget=forms.PasswordInput(attrs=
		{'class':'form-control','placeholder':"enter password"}))
	password2= forms.CharField(widget=forms.PasswordInput(attrs=
		{'class':'form-control','placeholder':"enter confirm password"}))
	class Meta:
		model=User
		fields = ['username','email']
		widgets={
		"username":forms.TextInput(attrs={'class':'form-control','placeholder':"enter username"}),
		"email":forms.EmailInput(attrs={'class':'form-control','placeholder':"example@gmail.com"}),
		
		}