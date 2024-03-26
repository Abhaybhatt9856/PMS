from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age=models.PositiveBigIntegerField(null=True)
    salary=models.FloatField(null=True)
    is_manager=models.BooleanField(default=False)
    is_developer=models.BooleanField(default=False)

    class Meta:
        db_table='user'



