from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


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

def view_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            # Create user
            form.save()

            # Manually authenticate the user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Compare hashed and raw data
            user = authenticate(username = username, password = raw_password)
            # Securely log in the user
            login(request, user)
            return redirect('login_page.html')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})