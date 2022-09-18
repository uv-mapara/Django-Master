from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse

def allow_user(allow=[]):
    def status(func):
        def wrap(request,*args,**kwargs):
            if request.allow:
                return func(request,*args,**kwargs)
            else:
                return PermissionDenied
        return wrap
    return status

def status(func):
    def wrap(request,*args,**kwargs):
        if request.status=='True':
            return func(request,*args,**kwargs)
        else:
            return 
    return wrap