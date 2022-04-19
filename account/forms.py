from dataclasses import fields
from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username',min_length=4,max_length=50,help_text='Required')
    email = forms.EmailField(max_length=100,help_text='Required',error_messages={'required':'Email is mandatory'})
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name','email',)
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder':'Username'}
        )
        self.fields['email'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder':'E-mail', 'name':'email'}
        )
        self.fields['password'].widget.attrs.update(
            {'class':'form-control mb-3', 'placeholder':'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class':'form-control', 'placeholder':'Repeat Password'}
        )
    
    def validate_duplicate_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        users = UserBase.objects.filter(user_name=user_name)
        if users.count():
            raise forms.ValidationError('Username already exists')
        return user_name
    
    def validate_repeat_password(self):
        formData = self.cleaned_data
        if(formData['password']!=formData['password2']):
            raise forms.ValidationError('Passwords do not match!')
        return formData['password2']


    def validate_duplicate_email(self):
        email = self.cleaned_data['email']
        if(UserBase.objects.filter(email=email).exists()):
            raise forms.ValidationError('Email already taken, please choose another one!')
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Email','id':'user_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','id':'login'}))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-username', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

class PasswordReForm(PasswordResetForm):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Email','id':'form-email'}))

    def clean_email(self):
        print('Hello')
        email = self.cleaned_data['email']
        try:
            required_user = UserBase.objects.get(email=email)
        except:
            pass
        return email


class PasswordReConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'New Password','id':'form-newpass'}))

    new_password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Repeat New Password','id':'form-newpass2'}))
    