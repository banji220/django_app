from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} your account has been created! You are now able to log in")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form":form})


@login_required
def profile(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        image_profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and image_profile_update_form.is_valid():
            user_update_form.save()
            image_profile_update_form.save()
            messages.success(request, "Your Profile has been updated")
            return redirect("profile")
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        image_profile_update_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        "u_form": user_update_form,
        "p_form": image_profile_update_form,
    }
    
    return render(request, "users/profile.html", context)