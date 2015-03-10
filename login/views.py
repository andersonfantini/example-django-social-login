# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from models import Usuario
from forms import LoginForm, CadastroForm

def criar_usuario(request):
	msg = ''
	form = CadastroForm(request.POST or None)
	if form.is_valid():
		form.save()
		msg = 'Salvo com Sucesso'
		try:
			subject = '[Diário de Vinhos] Seja bem vindo'
			#to = [form.email]
			#from_email = settings.DEFAULT_FROM_EMAIL
			#campos = { 'request': request, 'nome': form.nome}
			#message = get_template('email/email_cadastrado.html').render(Context(campos))
			#envio_email = EmailMessage(subject, message, to=to, from_email=from_email)
			#envio_email.content_subtype = 'html'
			#envio_email.send()
		except Exception, e:
			msg = 'Tivemos problemas ao enviar o e-mail'
	return render(request,"login/cadastro.html",{'form':form, 'msg':msg})

def login(request):
	form  = LoginForm()
	msg = ''
	form = LoginForm(request.POST or None)
	if form.is_valid():
		email = request.POST['email']
		password = request.POST['password']
		try:
			user = authenticate(email=email, password=password)
			if user is not None:
				if user.is_active:				
					auth_login(request, user)
					return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
				else:
					msg = 'Usuário Inativo!'
			else:
				msg = 'Usuário ou senha inválido!'			
		except Exception, e:
			msg = e
	return render(request,"login/login.html",{'form': form, 'msg':msg})

def logout_user(request):
	logout(request)
	return redirect('login')

@login_required
def home(request):
	return render(request,"login/home.html")

