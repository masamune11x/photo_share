from django import forms
from django.contrib.auth.models import User
from .models import CreateUser

# フォームクラス作成
class CreateUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(),label="Password")

    class Meta: 
        model = User
        field = ["username", "email", "password"]
        labels = {'username':"username",'email':"email"}


class AddUserForm(forms.ModelForm):
    class Meta():
        model = CreateUser
        




