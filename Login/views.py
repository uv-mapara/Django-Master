from django.shortcuts import render,redirect
from django.http import request,HttpResponseRedirect,HttpResponse
from .models import Member
from .forms import MemberForm
# from practice.decorator import status

# @status
def signin(request):
    if request.method=="POST":
        try:
            m = Member.objects.get(username=request.POST['username'])
            
            if m.password == request.POST['password']:
                return HttpResponseRedirect('/Login/index/')

            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password </a></h2>")
        except:
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'signin.html')

def index(request):
   return render(request,'index.html')

def signup(request):
    obj=MemberForm(request.POST)
    if obj.is_valid():
        obj.save()
    return render(request,'signup.html',{'obj':obj})
