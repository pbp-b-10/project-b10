from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pedulee.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.backends import UserModel
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
    if request.method == "POST":
      data = json.loads(request.body)
      username = data['username']
      password = data['password']
      email = data['email']
      firstname = data['firstname']
      lastname = data['lastname']
      
      try:
        user = User.objects.create_user(
          username = username, 
          email = email, 
          password = password,
          first_name = firstname,
          last_name = lastname,
        )
      except:
        user = User.objects.get(username = username)

      phone = data['phone']
      birthdate = data['birthdate']
      address = data['address']

      profile = Profile(
        user = user,
        phone = phone,
        birthdate = birthdate,
        address = address
      )
      
      profile.save()

      return JsonResponse({
              "status": True,
              "message": "Successfully created user!"
            }, status=200)
    else:
      return JsonResponse({
          "status": False,
          "message": "Failed to register."
        }, status=401)

#push