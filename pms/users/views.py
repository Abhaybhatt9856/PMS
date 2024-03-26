from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from .models import User
from projects.models import Project,User_task
from .forms import FormManagerRegistration,FormDeveloperRegistration
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
# Create your views here.


class ManagerRegistrationView(CreateView):
    model=User
    template_name='users/manager_registration.html'
    form_class=FormManagerRegistration
    success_url='/users/login'


class DeveloperRegistraionView(CreateView):
    model=User
    template_name='users/developer_registration.html'
    form_class=FormDeveloperRegistration
    success_url='/users/login'


class LoginPageView(LoginView):
    model=User
    template_name='users/login.html'
    
    def get_redirect_url(self) -> str:
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/users/man_dash/'
            else:
                return '/users/dev_dash/'

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')     
class ManagerDashboardView(ListView):
    model=Project
    context_object_name='projects'
    template_name='users/manager_dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = Project.objects.filter(project_status='Active').count() 
        context["completed"] = Project.objects.filter(project_status='Completed').count() 
        context["cancelled"] = Project.objects.filter(project_status='Cancelled').count() 
        context["Hold"] = Project.objects.filter(project_status='On Hold').count() 

        context["data_active"] = Project.objects.filter(project_status='Active') 
        context["data_completed"] = Project.objects.filter(project_status='Completed') 
        context["data_cancelled"] = Project.objects.filter(project_status='Cancelled') 
        context["data_Hold"] = Project.objects.filter(project_status='On Hold') 
        
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class DeveloperDashboardView(ListView):
    model=User_task
    template_name='users/developer_dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks_with_titles = User_task.objects.select_related('taksid').all().values('taksid__id', 'taksid__title','taksid__status','taksid__project')
        #get task from user
        context['data']=user_tasks_with_titles
        return context

