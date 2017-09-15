from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class Login(View):
    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user_pass = authenticate(username=username, password=password)
        if user_pass:
            return True
        return False