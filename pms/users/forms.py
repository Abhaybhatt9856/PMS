from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class FormManagerRegistration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email','age','salary','password1','password2']
    
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_manager=True
        user.save()
        return user

class FormDeveloperRegistration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email','age','salary','password1','password2']

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_developer=True
        user.save()
        return user