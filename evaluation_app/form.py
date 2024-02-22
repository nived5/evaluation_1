from django import forms
from django.contrib.auth.forms import UserCreationForm

from evaluation_app.models import Login, user, workmanager


class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields =('username','password1','password2')

class customer_Form(forms.ModelForm):
    class Meta:
            model = user
            fields = ('name','contact_no','email','address')
#
class work_manager_Form(forms.ModelForm):
    class Meta:
        model = workmanager
        fields = ('name','contact_no','email')
