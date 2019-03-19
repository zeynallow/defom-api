from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import accountCreationForm, accountChangeForm
from .models import account

class accountAdmin(UserAdmin):
    add_form = accountCreationForm
    form = accountChangeForm
    model = account
    list_display = ['email', 'username', 'name']

admin.site.register(account, accountAdmin)
