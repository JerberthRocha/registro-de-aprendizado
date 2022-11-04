from django.urls import path
from . import views

app_name = 'learning_logs'

"""Define padrões de URL para learning_logs."""

urlpatterns = [
    path('', views.index, name="index"), # Página inicial
]
