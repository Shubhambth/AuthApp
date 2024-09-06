from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth

User = get_user_model()

def home(request):
  
  return render(request,'auth_user/base.html')

def user_login(request):
  if request.method== "POST":
    username = request.POST.get("username") 
    password = request.POST.get("password") 
    if all([username,password]):
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect('home')
      
    

  return render(request,'auth_user/login_view.html',{})

def user_register(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
      user = User.objects.create_user(username=username,email=email,password=password)
      user.save()
      return redirect('loginu')
    except:
      return render(request,'auth_user/register.html',{})
  return render(request, 'auth_user/register.html',{})


def user_logout(request):
  auth.logout(request)
  return redirect('home')