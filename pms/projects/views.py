from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse,reverse_lazy
from django.views import View
from .models import Project,Project_team,User,Project_module,Task,User_task
from .forms import FormProject,FormProjectEdit,FormProjectTeam,FormCreateModule,FormTask,FormEditModule,FormEditTask,FormAssignTask
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
# Create your views here.

#Create Project
@method_decorator(login_required, name='dispatch')
class CreateProject(CreateView):
    model=Project
    form_class=FormProject
    template_name='projects/create_project.html'
    success_url='/users/man_dash/'

#ProjectList
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProjectList(ListView):
    model=Project
    context_object_name='project'
    template_name='projects/project_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = Project.objects.filter(project_status='Active').count() 
        context["completed"] = Project.objects.filter(project_status='Completed').count() 
        context["cancelled"] = Project.objects.filter(project_status='Cancelled').count() 
        context["Hold"] = Project.objects.filter(project_status='On Hold').count() 
        
        return context
    
#Project Show
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProjectShow(DetailView):
    model=Project
    context_object_name='project'
    template_name='projects/project_show.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id=self.kwargs['pk']
        context["developer"] =  Project_team.objects.filter(project=project_id)
        context["project_id"]=self.kwargs['pk']
        context["project_module"]=Project_module.objects.filter(project=project_id)
        return context
    


#Change Project Status
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ChangeProjectStatus(View):
    def post(self,request,pk,project_id,status):
        project_status=Project.objects.get(id=pk)
        print(status)
        if status == 'Active':
            project_status.project_status = "Active"
            project_status.save()
            return redirect(reverse('project_show',kwargs={'pk':self.kwargs['project_id']}))
        
        if status == 'Completed':
            project_status.project_status = "Completed"
            project_status.save()
            return redirect(reverse('project_show',kwargs={'pk':self.kwargs['project_id']}))
        
        if status == 'Cancelled':
            project_status.project_status = "Cancelled"
            project_status.save()
            return redirect(reverse('project_show',kwargs={'pk':self.kwargs['project_id']}))
        
        if status == 'On Hold':
            project_status.project_status = "On Hold"
            project_status.save()
            return redirect(reverse('project_show',kwargs={'pk':self.kwargs['project_id']}))
        
#Project Edit
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProjectEdit(UpdateView):
    model=Project
    form_class=FormProjectEdit
    template_name='projects/edit_project.html'
    def get_success_url(self) -> str:
        success_url = reverse_lazy('project_show', kwargs={'pk': self.kwargs['pk']})
        return success_url
    
#Create Project Team
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProjectTeam(CreateView):
    model=Project_team
    form_class=FormProjectTeam
    template_name='projects/project_team.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id') 
        context["developer"] = User.objects.filter(is_developer=True) 
        context["team_member"] = Project_team.objects.filter(project_id=project_id)
        context['delete_id']=project_id
        return context
    
    
    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')  # Assuming project_id is passed in URL
        # project_id = 1
        if project_id:
            project = Project.objects.get(pk=project_id)
            initial['project'] = project  # Set the project field with the retrieved project
        return initial
    
    def get_success_url(self) -> str:
        success_url=reverse_lazy('project_team', kwargs={'project_id':self.kwargs['project_id']})
        return success_url
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CreateProjectModule(CreateView):
    model=Project_module
    form_class=FormCreateModule
    template_name='projects/project_module.html'
    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')  # Assuming project_id is passed in URL
        if project_id:
            project = Project.objects.get(pk=project_id)
            initial['project'] = project  # Set the project field with the retrieved project
        return initial

    def get_success_url(self) -> str:
        project_id = self.kwargs.get('project_id')
        success_url = reverse_lazy('create_project_module', kwargs={'project_id': project_id})
        return success_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        context["module"] = Project_module.objects.filter(project=project_id)
        context["project_id"]=project_id
        return context
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')   
class ProjectModuleShow(DetailView):
    model=Project_module
    context_object_name='module'
    template_name='projects/project_show_module.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get("project_id")
        context['task']=Task.objects.filter(module=self.kwargs['pk'])
        
        return context
    
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class EditModule(UpdateView):
    model=Project_module
    form_class=FormEditModule
    template_name='projects/edit_module.html'
    def get_success_url(self) -> str:
        success_url=reverse_lazy('projecct_module_show',kwargs={'pk':self.kwargs['pk'],'project_id':self.kwargs['project_id']})
        return success_url

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CreateTask(CreateView):
    model=Task
    form_class=FormTask
    template_name='projects/create_task.html'
    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        module_id = self.kwargs.get('module_id')
        if project_id:
            project = Project.objects.get(pk=project_id)
            initial['project'] = project  
        
        if module_id:
            module=Project_module.objects.get(pk=module_id)
            initial['module']=module
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        module_id=self.kwargs['module_id']
        project_id = self.kwargs.get('project_id')
        context["task"] = Task.objects.filter(module=module_id) 
        context['project_id']=project_id
        context['module_id']=module_id
        return context
    
    def get_success_url(self) -> str:
        success_url=reverse_lazy('create_task',kwargs={'project_id':self.kwargs['project_id'],'module_id':self.kwargs['module_id']})
        return success_url

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')  
class ShowTask(DetailView):
    model=Task
    template_name='projects/show_task.html'
    context_object_name='task'

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ChangeTaskStatus(View):
     def post(self,request,pk,status):
        task_status=Task.objects.get(id=pk)
        print(status)
        if status == 'Not Started':
            task_status.status = "Not Started"
            task_status.save()
            return redirect(reverse('show_task',kwargs={'pk':self.kwargs['pk']}))
        
        if status == 'Progress':
            task_status.status = "Progress"
            task_status.save()
            return redirect(reverse('show_task',kwargs={'pk':self.kwargs['pk']}))
        
        if status == 'complete':
            task_status.status = "complete"
            task_status.save()
            return redirect(reverse('show_task',kwargs={'pk':self.kwargs['pk']}))

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')      
class EditTask(UpdateView):
    model=Task
    form_class=FormEditTask
    template_name='projects/edit_task.html'
    def get_success_url(self) -> str:
        success_url=reverse_lazy('show_task',kwargs={'pk':self.kwargs['pk']})
        return success_url

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class AssignTask(CreateView):
    model=User_task
    form_class=FormAssignTask
    template_name='projects/assign_task.html'
    def get_initial(self):
        initial = super().get_initial()
        task_id=self.kwargs.get('task_id')
        print(task_id)
        if task_id:
            task = Task.objects.get(pk=task_id)
            initial['taksid'] = task  
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        module_id=self.kwargs.get('module_id')
        context["task"] = Task.objects.filter(module=module_id)
        return context
    
    
    def get_success_url(self) -> str:
        success_url=reverse_lazy('projecct_module_show',kwargs={'pk':self.kwargs['module_id'],'project_id':self.kwargs['project_id']})
        return success_url

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class UpdateStatusView(View):
    def post(self, request, pk):
        # Get the task instance
        task = Task.objects.get(id=pk)
        if task.status == "Not Started":
            task.status = "Progress"
        elif task.status == "Progress":
            task.status = "complete"
      
        task.save()
        
        return redirect(reverse('dev_dash'))

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')  
class ProjectReport(DetailView):
    model=Project
    context_object_name='project'
    template_name='projects/project_report.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.filter(project=self.kwargs['pk'])
        return context
    













# this
# is 
# Delete
#delete Project Member

class DeleteProjectMember(DeleteView):
    model=Project_team
    template_name='delete.html'
    def get_success_url(self) -> str:
           print(self.kwargs['project_id'])
           success_url=reverse_lazy('project_team', kwargs={'project_id':self.kwargs['project_id']})
           return success_url

class DeleteModuleFromCreateModule(DeleteView):
    model=Project_module
    template_name='delete.html'
    def get_success_url(self) -> str:
        success_url=reverse_lazy('create_project_module',kwargs={'project_id':self.kwargs['project_id']})
        return success_url
    
class DeleteModule(DeleteView):
    model=Project_module
    template_name='delete.html'
    def get_success_url(self) -> str:
        success_url=reverse_lazy('project_show',kwargs={'pk':self.kwargs['project_id']})
        return success_url
    
class DeleteTaskFromCreateTask(DeleteView):
    model=Task
    template_name='delete.html'
    def get_success_url(self) -> str:
        success_url=reverse_lazy('create_task',kwargs={'project_id':self.kwargs['project_id'],'module_id':self.kwargs['module_id']})
        return success_url

class DeleteTask(DeleteView):
    model=Task
    template_name='delete.html'
    def get_success_url(self) -> str:
        success_url=reverse_lazy('projecct_module_show',kwargs={'pk':self.kwargs['module_id'],'project_id':self.kwargs['project_id']})
        return success_url

    