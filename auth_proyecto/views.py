from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

#----------------------------------------------------------------------------------

def auth_login(request):
	template_name = 'login.html'
	data = {}
	logout(request)
	username = password = ''
	
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(
			username=username,
			password=password
		)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('pyp:index')
			else:
				messages.error(
					request,
					'Usuario o Contraseña Incorrectos!'
					)
		else:
			messages.error(
				request,
				'Usuario o Contraseña Incorrectos!'
			)

	return render(request,template_name,data)


#----------------------------------------------------------------------------------

def auth_logout(request):
	logout(request)
	return redirect('auth:login')

