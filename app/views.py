from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm


def task_list(request):
    """
    Vista para listar todas las tareas con filtros y búsqueda.
    Implementa funcionalidad de filtrado por estado, prioridad y búsqueda por título.
    """
    tasks = Task.objects.all()
    
    # Filtros
    estado_filter = request.GET.get('estado')
    prioridad_filter = request.GET.get('prioridad')
    search_query = request.GET.get('search')
    
    if estado_filter:
        tasks = tasks.filter(estado=estado_filter)
    
    if prioridad_filter:
        tasks = tasks.filter(prioridad=prioridad_filter)
    
    if search_query:
        tasks = tasks.filter(
            Q(titulo__icontains=search_query) | 
            Q(descripcion__icontains=search_query)
        )
    
    # Paginación
    paginator = Paginator(tasks, 10)  # 10 tareas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas para el dashboard
    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(estado='pendiente').count()
    completed_tasks = Task.objects.filter(estado='completada').count()
    overdue_tasks = Task.objects.filter(
        fecha_limite__lt=timezone.now(),
        estado__in=['pendiente', 'en_progreso']
    ).count()
    
    context = {
        'page_obj': page_obj,
        'estado_filter': estado_filter,
        'prioridad_filter': prioridad_filter,
        'search_query': search_query,
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
    }
    
    return render(request, 'app/list.html', context)


def task_detail(request, pk):
    """
    Vista para mostrar los detalles de una tarea específica.
    """
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'app/task_detail.html', {'task': task})


def task_create(request):
    """
    Vista para crear una nueva tarea.
    Maneja tanto GET (mostrar formulario) como POST (procesar datos).
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Tarea "{task.titulo}" creada exitosamente.')
            return redirect('app:task_detail', pk=task.pk)
    else:
        form = TaskForm()
    
    return render(request, 'app/task_form.html', {
        'form': form,
        'title': 'Crear Nueva Tarea',
        'submit_text': 'Crear Tarea'
    })


def task_update(request, pk):
    """
    Vista para actualizar una tarea existente.
    """
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Tarea "{task.titulo}" actualizada exitosamente.')
            return redirect('app:task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'app/task_form.html', {
        'form': form,
        'task': task,
        'title': f'Editar Tarea: {task.titulo}',
        'submit_text': 'Actualizar Tarea'
    })


def task_delete(request, pk):
    """
    Vista para eliminar una tarea.
    Muestra confirmación antes de eliminar.
    """
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task_title = task.titulo
        task.delete()
        messages.success(request, f'Tarea "{task_title}" eliminada exitosamente.')
        return redirect('app:task_list')
    
    return render(request, 'app/task_confirm_delete.html', {'task': task})


def task_toggle_status(request, pk):
    """
    Vista AJAX para cambiar rápidamente el estado de una tarea.
    Útil para marcar tareas como completadas desde la lista.
    """
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        task = get_object_or_404(Task, pk=pk)
        
        # Lógica para cambiar estado
        if task.estado == 'pendiente':
            task.estado = 'en_progreso'
        elif task.estado == 'en_progreso':
            task.estado = 'completada'
        elif task.estado == 'completada':
            task.estado = 'pendiente'
        
        task.save()
        
        return JsonResponse({
            'success': True,
            'new_status': task.get_estado_display(),
            'status_class': task.estado
        })
    
    return JsonResponse({'success': False})


def dashboard(request):
    """
    Vista del dashboard principal con estadísticas y tareas recientes.
    """
    # Tareas recientes (últimas 5)
    recent_tasks = Task.objects.all()[:5]
    
    # Tareas vencidas
    overdue_tasks = Task.objects.filter(
        fecha_limite__lt=timezone.now(),
        estado__in=['pendiente', 'en_progreso']
    ).order_by('fecha_limite')
    
    # Tareas de alta prioridad pendientes
    high_priority_tasks = Task.objects.filter(
        prioridad__in=['alta', 'urgente'],
        estado__in=['pendiente', 'en_progreso']
    ).order_by('fecha_limite')
    
    # Estadísticas por estado
    status_stats = {}
    for status_code, status_name in Task.STATUS_CHOICES:
        count = Task.objects.filter(estado=status_code).count()
        status_stats[status_name] = count
    
    # Estadísticas por prioridad
    priority_stats = {}
    for priority_code, priority_name in Task.PRIORITY_CHOICES:
        count = Task.objects.filter(prioridad=priority_code).count()
        priority_stats[priority_name] = count
    
    context = {
        'recent_tasks': recent_tasks,
        'overdue_tasks': overdue_tasks,
        'high_priority_tasks': high_priority_tasks,
        'status_stats': status_stats,
        'priority_stats': priority_stats,
    }
    
    return render(request, 'app/dashboard.html', context)
