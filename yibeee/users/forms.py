from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # Class meta give us a nested namespace for configurations
    # and keeps the configurations in one place.
    # Within the configuration, we're saying that:
    # the model will be affected is the user model,
    # (for example form.save() is going to save it to user model)
    # and the fileds we have here in the below list
    # are the fileds  we want in the form and in what order.
    class Meta:
        model = User
        # password1 is the setting for password
        # password2 it the password confirmation
        fields = ['username','email','password1','password2']