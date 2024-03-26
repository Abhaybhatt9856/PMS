from django.db import models
from users.models import User
# Create your models here.

techChoices =(
    ("Python","Python"),
    ("Java","Java"),
    ("C++","C++"),
    ("C#","C#"),
)

projectStatus=(
    ('Active','Active'),
    ('Completed','Completed'),
    ('Cancelled','Cancelled'),
    ('On Hold','On Hold'),
)
class Project(models.Model):
    title=models.CharField( max_length=100)
    description=models.TextField()
    technology=models.CharField( max_length=100,choices=techChoices)
    estimated_hours=models.PositiveIntegerField()
    start_date=models.DateField()
    complateion_date=models.DateField()
    project_status=models.CharField( max_length=50, choices=projectStatus,default='Active')

    class Meta:
        db_table='Projects'

    def __str__(self):
        return self.title
    

class Project_team(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    #in future you should use many to many field for user
    
    class Meta:
        db_table = "project_team"
        
    
    def __str__(self):
        return self.user.username  
    


class Project_module(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    module_name=models.CharField( max_length=50)
    description=models.TextField()
    estimated_hours=models.PositiveIntegerField()
    start_date=models.DateField( auto_now_add=False)

    class Meta:
        db_table="project_module"

    def __str__(self) -> str:
        return self.module_name

status_option=(
    ('Not Started','Not Started'),
    ('Progress','Progress'),
    ('complete','complete'),
)

class Task(models.Model):
    module=models.ForeignKey(Project_module, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    title=models.CharField( max_length=50)
    priority=models.CharField( max_length=50)
    description=models.TextField()
    status=models.CharField( max_length=50, choices=status_option)
    estimated_minutes=models.PositiveIntegerField()
    total_util_time=models.PositiveIntegerField()

    class Meta:
        db_table='task'

    def __str__(self) -> str:
        return self.title
    
class User_task(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    taksid=models.OneToOneField(Task, on_delete=models.CASCADE)
