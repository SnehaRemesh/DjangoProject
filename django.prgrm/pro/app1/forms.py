from django.contrib.auth.forms import UserCreationForm
from app1.models import CustomUser,Book
from django import forms 
class CustomForms(UserCreationForm):
    class Meta(UserCreationForm.Meta):
                model=CustomUser
                fields=UserCreationForm.Meta.fields+('email','phone','address')
class Bookform(forms.ModelForm):
    class Meta:
           model=Book
           fields='__all__'