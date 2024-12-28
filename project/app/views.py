from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth

# Create your views here.
def reg(request):
    if request.method=='POST':
       username=request.POST['name']
       password=request.POST['password']
       email=request.POST['email']
       data=User.objects.create_user(username=username,email=email,password=password)
       data.save()
       return redirect(log)
    return render(request,'register.html')

def log(request):
    if request.method=='POST':
       username=request.POST['username']   
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       print(user)
       if user is not None:
           auth.login(request,user)
           return redirect(upload_file)
       else:
           return redirect(log)
    return render(request,'login.html')


def home(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'home.html',{'user':user})
    else:
        return redirect(log)    


    
def logout(request):
    if '_auth_user_id' in request.session:
        auth.logout(request)
        return redirect(log)
    else:
        return redirect(log)
    
def upload_file(request):
    photo=files.objects.all()
    rev=reversed(list(photo))
    
    if request.method=='POST':
        filename=request.FILES['file']
        data=files.objects.create(file=filename)
        data.save()
        return redirect(upload_file)
    return render(request,'home.html')
   