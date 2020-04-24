from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, UserUpdateForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Yor account has been created ! You are now allowed to Log In !')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST' :
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Yor account has been created !')
            return redirect('users/profile.html')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    stuff_for_frontend = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    } 

    return render(request, 'users/profile.html', stuff_for_frontend)