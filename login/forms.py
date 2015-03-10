# -*- coding: utf-8 -*-

from django import forms
from models import Usuario

class LoginForm(forms.Form):
	email = forms.EmailField(label="E-mail")
	password = forms.CharField(widget=forms.PasswordInput)

class CadastroForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(required=True)	
	password = forms.CharField(widget=forms.PasswordInput, label="Informe a Senha")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Confirme a Senha")

	class Meta:
		model = Usuario
		fields = ( 'username' , 'email', 'password', 'password2')

	def clean(self):
		cleaned_data = super(CadastroForm, self).clean()
		if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['password2']:
				raise forms.ValidationError("A confirmação de Senha não confere, tente novamente.")
		return self.cleaned_data

	def save(self,commit=True):
		user = super(CadastroForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()

		return user