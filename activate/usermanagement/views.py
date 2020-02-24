from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


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
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create user
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'usermanagement/signup.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'usermanagement/profile.html')


@login_required
def view_modify_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('view_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'usermanagement/modify_profile.html', context)
