from django import forms
from app1.models import Register_Data

class RegisterForm(forms.ModelForm):
    class Meta:
        model =  Register_Data
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Register_Data
        fields = ['email','passw']