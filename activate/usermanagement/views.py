from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout


# Create your views here.
def view_login(request):
    # Check if the user just wants to see the login page or is trying to login
    if request.method == 'POST':
        # The user has sent a login-form
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)

    return render(request, 'usermanagement/login_page.html')


def view_logout(request):
    logout(request)
    response = redirect('/login/')
    return response
