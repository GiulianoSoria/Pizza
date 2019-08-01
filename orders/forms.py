from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
    
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=64, required=True)
    last_name = forms.CharField(label='Last Name', max_length=64, required=True)
    email = forms.EmailField(label='Email', required=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control col-lg-6'
        self.fields['first_name'].widget.attrs['class'] = 'form-control col-lg-6'
        self.fields['last_name'].widget.attrs['class'] = 'form-control col-lg-6'
        self.fields['email'].widget.attrs['class'] = 'form-control col-lg-6'
        self.fields['password1'].widget.attrs['class'] = 'form-control col-lg-6'
        self.fields['password2'].widget.attrs['class'] = 'form-control col-lg-6'
        