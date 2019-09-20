from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class User_Creation_Form(UserCreationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)












# Кажись уже не надо
# class RegForm(forms.Form):
#     Username = forms.CharField()
#     Email = forms.EmailField(widget=forms.EmailInput(attrs={'kek': 'kek'}))
#     Password = forms.CharField()
#
#
# class Login(forms.Form):
#     username = forms.CharField(label='Username',
#                                   widget=forms.TextInput(
#                                           {'value': 'Username'})
#                                   )
#     password = forms.CharField()
