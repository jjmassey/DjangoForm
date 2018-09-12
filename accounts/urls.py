from django.urls import path
from . import views
from django.contrib.auth import login
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', TemplateView.as_view(template_name="accounts/login.html"), name='login')
]
