from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_detail(request):
    if request.user.is_authenticated:

        return render(request, 'users_detail.html')
    else:
        return redirect('login_view')

def login_view(request):
    if request.method == "GET":

        return render(request, 'users_login.html')

    elif request.method == "POST":

        user_id = request.POST.get('id')
        user_pw = request.POST.get('password')

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user=user)
            return redirect('user_detail')
        else:
            return redirect('login_view')

