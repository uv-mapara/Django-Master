from django.shortcuts import render,redirect
from app1.models import Register_Data
from app1.forms import RegisterForm,LoginForm
from django.http import HttpResponseRedirect
# Create your views here.
def show(request):
    if request.session.keys():
        data = Register_Data.objects.all()
        return render(request,'show.html',{'data':data})
    else:
        return HttpResponseRedirect('/app1/login1/')

def login1(request):
    form = LoginForm(request.POST or None)
    if request.POST:
        uemail = request.POST['email']
        password = request.POST['pass']
        try:
            data = Register_Data.objects.get(email=uemail,passw=password)
            if data:
                request.session['name'] = data.name
                #request.session['email'] = data.email
                return redirect('show')
            else:
                return HttpResponseRedirect('/app1/login1/')
        except:
            return HttpResponseRedirect('/app1/login1/')
    return render(request,'login1.html',{'form':form})

def logout(request):
    if request.session.keys():
        request.session.flush()
        return HttpResponseRedirect('/app1/login1/')
    else:
        return HttpResponseRedirect('/app1/login1/')
    
def register(request):
    form = RegisterForm(request.POST or None)
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if request.session.keys():
                return redirect('show')
            return HttpResponseRedirect('/app1/login1/')
    return render(request,'register.html',{'form':form})
    
def update(request,id):
    if request.session.keys():
        profile = Register_Data.objects.get(id=id)
        form = RegisterForm(instance=profile,data=request.POST or None)
        # if request.POST:
        #     form = RegisterForm(instance=profile,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        return render(request,'register.html',{'form':form})
    else:
        return HttpResponseRedirect('/app1/login1/')
    
def delete(request,pk):
    if request.session.keys():
        delete_id = Register_Data.objects.get(id=pk)
        delete_id.delete()
        return redirect('show')
    else:
        return HttpResponseRedirect('/app1/login1/')