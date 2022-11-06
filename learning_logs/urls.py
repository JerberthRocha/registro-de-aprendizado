from django.urls import path
from . import views

app_name = 'learning_logs'

"""Define padrões de URL para learning_logs."""

urlpatterns = [
    path('', views.index, name="index"), # Página inicial
    path('topics/', views.topics, name='topics'), # Mostra todos os assuntos
    path('new_topic/', views.new_topic, name='new_topic'), # # Página para adicionar um novo assunto
    path('topics/<int:id>/', views.topic, name='topic'), # Página de detalhes para um único assunto
    path('new_entry/<int:id>/', views.new_entry, name='new_entry'), # Página para adicionar uma nova entrada
]
