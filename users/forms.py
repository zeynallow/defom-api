from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import account

class accountCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = account
        fields = ('username', 'email')

class accountChangeForm(UserChangeForm):

    class Meta:
        model = account
        fields = UserChangeForm.Meta.fields
