from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
		self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
		self.fields['password1'].help_text = ""
		self.fields['email'].widget.attrs['placeholder'] = 'email'
        