from django import forms
from .models import Project,Project_team,Project_module,Task,User_task

class FormProject(forms.ModelForm):
    class Meta:
        model=Project
        fields="__all__"

class FormProjectEdit(forms.ModelForm):
    class Meta:
        model=Project
        fields="__all__"

class FormProjectTeam(forms.ModelForm):
    class Meta:
        model=Project_team
        fields='__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['project'].widget.attrs['disabled'] = True
    
class FormCreateModule(forms.ModelForm):
    class Meta:
        model=Project_module
        fields="__all__"
        
class FormEditModule(forms.ModelForm):
    class Meta:
        model=Project_module
        fields="__all__"

class FormTask(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"

class FormEditTask(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"

class FormAssignTask(forms.ModelForm):
    class Meta:
        model=User_task
        fields="__all__"

