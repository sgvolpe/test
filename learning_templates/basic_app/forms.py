from django import forms
from django.core import validators
from basic_app.models import User
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class NewUserForm(forms.ModelForm):

    new_field = forms.CharField()
    class Meta:

        model = User
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
