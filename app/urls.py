from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # Dashboard principal
    path('', views.dashboard, name='dashboard'),
    
    # CRUD de tareas
    path('tareas/', views.task_list, name='task_list'),
    path('tareas/crear/', views.task_create, name='task_create'),
    path('tareas/<int:pk>/', views.task_detail, name='task_detail'),
    path('tareas/<int:pk>/editar/', views.task_update, name='task_update'),
    path('tareas/<int:pk>/eliminar/', views.task_delete, name='task_delete'),
    
    # Funcionalidades adicionales
    path('tareas/<int:pk>/toggle-status/', views.task_toggle_status, name='task_toggle_status'),
]
