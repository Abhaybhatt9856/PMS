from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Project_team)
admin.site.register(Project_module)
admin.site.register(Task)
admin.site.register(User_task)
