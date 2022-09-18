from django.shortcuts import render,redirect
from .models import Admin
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "GET":
        if request.session.has_key('admin'):
            return redirect('dashboard')
        else:
            return render(request, 'session/index.html', {})
    if request.method == "POST":
        name = ''
        lname = ''
        email = request.POST['email']
        pwd = request.POST['password']
        e = Admin.objects.filter(email=email)
        p = Admin.objects.filter(password=pwd)
        if e and p:
            admin = Admin.objects.filter(email=email)
            for a in admin:
                name = a.name
                lname = a.last_name
            request.session["admin"] = "Admin"
            request.session['name'] = name
            request.session['lname'] = lname
            request.session["email"] = email
            return redirect('dashboard')
        else:
            messages.warning(request,message="Invalid Email or Password!")
            return render(request, 'session/index.html', {})

def dashboard(request):
    if 'admin' in request.session:
            return render(request, 'session/dashboard.html', {})
    else:
        messages.warning(request, message="Please login to continue!")
        return redirect('index')
    
#logout
def logout(request):
    if 'admin' in request.session:
        del request.session["admin"]
        del request.session["name"]
        del request.session["lname"]
        del request.session["email"]
        request.session.flush()
        return redirect('index')
    else:
        return redirect('index')