from django import forms
from django.core import validators
from first_app.models import User

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
