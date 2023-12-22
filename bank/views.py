import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import Form
from .models import Branch


def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save()
                return redirect('login')
        else:
            messages.info(request,'password didnot match' )
            return redirect('register')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def welcome(request):
    return render(request,'welcome.html')

def form(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Application Accepted')
        else:
            print(form.errors)
            messages.error(request,'Form Submission Failed, Please Fill The Form Corectly')
    return render(request,'forms.html',{'form':form})


def getbranches(request):
    data=json.loads(request.body)
    district_id=data["id"]
    branches=Branch.objects.filter(district__id=district_id)
    return JsonResponse(list(branches.values("id","name")), safe=False)


def success(request):
    return render(request,'success.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

