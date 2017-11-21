from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def user_login(request):
	if request.user.is_authenticated():
		messages.info('Ya has iniciado sesion')
		return HttpResponseRedirect('/')

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')

	return render(request, 'registration/login.html')


def home(request):
    return render(request, 'users/home.html')
