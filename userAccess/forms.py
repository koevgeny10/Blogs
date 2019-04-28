from django import forms

# Кажись уже не надо
class RegForm(forms.Form):
    Username = forms.CharField()
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'kek': 'kek'}))
    Password = forms.CharField()


class Login(forms.Form):
    username = forms.CharField(label='Username',
                                  widget=forms.TextInput(
                                          {'value': 'Username'})
                                  )
    password = forms.CharField()
