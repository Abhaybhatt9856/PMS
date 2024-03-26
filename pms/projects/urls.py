from django.urls import path
from .views import CreateProject,ProjectList,ProjectShow,ChangeProjectStatus,ProjectEdit,ProjectTeam,DeleteProjectMember,CreateProjectModule,DeleteModuleFromCreateModule,DeleteModule,ProjectModuleShow,CreateTask,EditModule,DeleteTaskFromCreateTask,ShowTask,ChangeTaskStatus,EditTask,DeleteTask,AssignTask,UpdateStatusView,ProjectReport
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('create_project/',CreateProject.as_view(),name='create_project'),
   path('project_list/',ProjectList.as_view(),name='project_list'),
   path('project_show/<int:pk>',ProjectShow.as_view(),name='project_show'),
   path('change_project_status/<int:pk>/<int:project_id>/<str:status>',ChangeProjectStatus.as_view(),name='change_project_status'),
   path('project_edit/<int:pk>/',ProjectEdit.as_view(),name='project_edit'),
   path('project_team/<int:project_id>/',ProjectTeam.as_view(),name='project_team'),
   path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
   path('delete_team_memeber/<int:pk>/<int:project_id>/',DeleteProjectMember.as_view(),name='delete_team_memeber'),
   path('create_project_module/<int:project_id>/',CreateProjectModule.as_view(),name='create_project_module'),
   path('delete_module_from_createModule/<int:pk>/<int:project_id>/',DeleteModuleFromCreateModule.as_view(),name='delete_module_from_createModule'),
   path('delete_module/<int:pk>/<int:project_id>/',DeleteModule.as_view(),name='delete_module'),
   path('projecct_module_show/<int:pk>/<project_id>/',ProjectModuleShow.as_view(),name='projecct_module_show'),
   path('create_task/<project_id>/<module_id>/',CreateTask.as_view(),name='create_task'),
   path('edit_module/<int:pk>/<int:project_id>',EditModule.as_view(),name='edit_module'),
   path('delete_task_from_create_task/<int:pk>/<project_id>/<module_id>/',DeleteTaskFromCreateTask.as_view(),name='delete_task_from_create_task'),
   path('show_task/<int:pk>',ShowTask.as_view(),name='show_task'),
   path('change_task_status/<int:pk>/<str:status>/',ChangeTaskStatus.as_view(),name='change_task_status'),
   path('edit_task/<int:pk>/',EditTask.as_view(),name='edit_task'),
   path('delete_task/<int:pk>/<int:module_id>/<int:project_id>',DeleteTask.as_view(),name='delete_task'),
   path('assign_task/<int:task_id>/<module_id>/<project_id>',AssignTask.as_view(),name='assign_task'),
   path('update_status/<int:pk>',UpdateStatusView.as_view(),name='update_status'),
   path('project_report/<int:pk>/',ProjectReport.as_view(),name='project_report'),
]
