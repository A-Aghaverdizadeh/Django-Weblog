from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, views
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserRegistrationForm,\
                        UserEditForm, ProfileEditForm
from django.core.paginator import Paginator, EmptyPage,\
											PageNotAnInteger
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse
from bloghome.models import Post

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Authenticated Successfully')
                    return redirect('dashboard')
                else:
                    messages.error(request, "Your username and password didn't match Please try again")
            else:
                messages.error(request, 'Invalid Login')
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'account/login.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 
                                'account/register_done.html',
                                {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': user_form})

@login_required
def dashboard(request):
    context = {'section': 'dashboard'}
    return render(request, 'account/dashboard.html', context)

def logout(request):
    logout_response = views.LogoutView.as_view()(request)
    messages.success(request, 'You have been logged out successfully.')

    return redirect('user_login')

@login_required
def edit(request):
    profile = Profile.objects.all()
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                instance=request.user.profile)

    context = {'user_form': user_form, 
                        'profile_form': profile_form,
                        'profile': profile}
    return render(request, 'account/edit.html', context)

@login_required
def profile(request, user_name):
    user = get_object_or_404(User, 
                             username=user_name)
    posts = Post.published.filter(author=user)
    profile_url = reverse('profile', kwargs={'user_name': user_name})


    context = {'user': user, 
                'profile_url': profile_url,
                'posts': posts}
    return render(request, 'account/profile.html', context)

