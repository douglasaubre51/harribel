from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.db import IntegrityError

from .models import Account

# Create your views here.
def get_sign_up_page(request):

    if request.method == 'GET':
        return render(request,'sign-up.html')

    if request.method == 'POST':
        username = request.POST.get('username_box',False)
        password = request.POST.get('password_box',False)
        print(f'username:{username}')
        print(f'password:{password}')

        if username and password :
            try:
                user = Account.objects.create_user(username = username)
                user.set_password(password)
                user.save()
                return redirect('/')

            except IntegrityError:
                error_msg = 'username already exists!'
                return render(request,'sign-up.html',{ 'error':error_msg })

        else:
            error_msg = 'enter all fields!'
            return render(request,'sign-up.html',{ 'error':error_msg })

def get_login_page(request):

    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        username = request.POST.get('username_box',False)
        password = request.POST.get('password_box',False)
        print(f'username:{username}')
        print(f'password:{password}')

        user = authenticate(username = username,password = password)

        if user:
            login(request,user)
            return redirect('chat/')

        else:
            error_message = 'invalid username or password!'
            return render(request,'login.html',{ 'error':error_message })
