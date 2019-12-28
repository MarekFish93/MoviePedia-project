from django import forms
from . models import UserProfileInfo
from db.models import Film
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
        
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('profile_pic',)

class FilmListForm(forms.ModelForm):
    class Meta():
        model = Film
        fields = ('title', 'year')
