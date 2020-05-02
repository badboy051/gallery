from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import SignUpForm

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username=form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password,email=email)
        user.groups.set([Group.objects.get(name='simple_user')])
        user.is_staff=True
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})
# Create your views here.
