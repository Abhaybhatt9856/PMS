from django.urls import path
from .views import ManagerRegistrationView,DeveloperRegistraionView,LoginPageView,ManagerDashboardView,DeveloperDashboardView

urlpatterns = [
    path('man_reg/',ManagerRegistrationView.as_view(),name='man_reg'),
    path('dev_reg/',DeveloperRegistraionView.as_view(),name='dev_reg'),
    path('login/',LoginPageView.as_view(),name='login'),
    path('man_dash/',ManagerDashboardView.as_view(),name='man_dash'),
    path('dev_dash/',DeveloperDashboardView.as_view(),name='dev_dash'),
]
