from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request, 'register.html')
    
    def post(self,request):
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = User.objects.filter(username = username)
        if user.exists():
            print('user already exist')
            return redirect('/accounts/register')
        User.objects.create_user(username=username, password=password) 
        return redirect('/accounts/login/')

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self,request):
        username = request.POST.get("uname")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)