from django.urls import re_path as url
from django.contrib.auth.views import LoginView
from . import views

"""Define padrões de URL para users"""

app_name = 'users'

urlpatterns = [
    url(
        'login/', 
        LoginView.as_view(template_name='users/pages/login.html'), 
        name='login'
    ), # Página de login
]
