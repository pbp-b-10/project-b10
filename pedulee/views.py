import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ExtendedUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfileForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            messages.success(request, 'Your account has been successfully created!')
            return redirect('pedulee:login')
    else:
        form = ExtendedUserCreationForm()
        profile_form = ProfileForm()

        
    context = {'form':form, 'profile_form':profile_form}
    return render(request, 'signup.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("pedulee:show_pedulee")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username or Password is wrong!')
    context = {}
    return render(request, 'signin.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('pedulee:login'))
    response.delete_cookie('last_login')
    return response