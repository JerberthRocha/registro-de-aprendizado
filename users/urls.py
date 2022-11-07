from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

"""Define padrões de URL para users"""

app_name = 'users'

urlpatterns = [
    url(
        'login/', 
        LoginView, 
        {'template_name': 'users/pages/login.html'}, 
        name='login'
    ), # Página de login
]
