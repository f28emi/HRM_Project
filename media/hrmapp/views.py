from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Place
from .models import Team
# Create your views here.





def login(request):
    if request.method =='POST':
        userName = request.POST['UserName']
        password = request.POST['Password']
        user=auth.authenticate(username=userName,password=password)

        if user is None:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

        else:
            auth.login(request, user)
            return redirect('/')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        userName=request.POST['UserName']
        firstName=request.POST['FirstName']
        lastName=request.POST['LastName']
        email = request.POST['Email-id']
        password = request.POST['Password']
        cpassword = request.POST['Password1']
        if password==cpassword:
            if User.objects.filter(username=userName).exists():
                messages.info(request,"UserName  Already Exists")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, " Email-ID Already Exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=userName,password=password,first_name=firstName,last_name=lastName,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')

    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')



def home(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})