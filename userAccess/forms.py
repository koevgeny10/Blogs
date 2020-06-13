from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class MyUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
