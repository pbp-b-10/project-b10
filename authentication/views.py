from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pedulee.models import Profile
from django.contrib.auth.models import User
import json

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def logout(request):
    try:
      logout(request)
      return JsonResponse({
              "status": True,
              "message": "Successfully Logged Out!"
            }, status=200)
    except:
      return JsonResponse({
          "status": False,
          "message": "Failed to Logout."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Gagal woi'})
        User.objects.create_user(username=username, password=password1, email=email)
        return JsonResponse({'status': 'success'})