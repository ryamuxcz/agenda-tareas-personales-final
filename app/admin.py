from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Task.
    Proporciona una interfaz administrativa completa para gestionar tareas.
    """
    
    list_display = [
        'titulo', 
        'prioridad', 
        'estado', 
        'fecha_limite', 
        'dias_restantes',
        'esta_vencida',
        'fecha_creacion'
    ]
    
    list_filter = [
        'prioridad',
        'estado',
        'fecha_creacion',
        'fecha_limite',
        'completada_en'
    ]
    
    search_fields = [
        'titulo',
        'descripcion'
    ]
    
    list_editable = [
        'prioridad',
        'estado'
    ]
    
    readonly_fields = [
        'fecha_creacion',
        'fecha_actualizacion',
        'completada_en',
        'dias_restantes',
        'esta_vencida'
    ]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Estado y Prioridad', {
            'fields': ('prioridad', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_limite', 'fecha_creacion', 'fecha_actualizacion', 'completada_en')
        }),
        ('Información Calculada', {
            'fields': ('dias_restantes', 'esta_vencida'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['-fecha_creacion']
    
    date_hierarchy = 'fecha_creacion'
    
    actions = ['marcar_como_completadas', 'marcar_como_pendientes', 'cambiar_prioridad_alta']
    
    def marcar_como_completadas(self, request, queryset):
        """Acción personalizada para marcar tareas como completadas."""
        updated = queryset.update(estado='completada')
        self.message_user(
            request,
            f'{updated} tarea(s) marcada(s) como completada(s).'
        )
    marcar_como_completadas.short_description = "Marcar como completadas"
    
    def marcar_como_pendientes(self, request, queryset):
        """Acción personalizada para marcar tareas como pendientes."""
        updated = queryset.update(estado='pendiente')
        self.message_user(
            request,
            f'{updated} tarea(s) marcada(s) como pendiente(s).'
        )
    marcar_como_pendientes.short_description = "Marcar como pendientes"
    
    def cambiar_prioridad_alta(self, request, queryset):
        """Acción personalizada para cambiar prioridad a alta."""
        updated = queryset.update(prioridad='alta')
        self.message_user(
            request,
            f'{updated} tarea(s) con prioridad cambiada a alta.'
        )
    cambiar_prioridad_alta.short_description = "Cambiar prioridad a alta"
    
    def get_queryset(self, request):
        """Optimizar consultas del admin."""
        return super().get_queryset(request).select_related()
    
    def save_model(self, request, obj, form, change):
        """Personalizar el guardado en el admin."""
        super().save_model(request, obj, form, change)
        
        # Log de cambios importantes
        if change:
            if 'estado' in form.changed_data:
                self.message_user(
                    request,
                    f'Estado de "{obj.titulo}" cambiado a {obj.get_estado_display()}.'
                )
            if 'prioridad' in form.changed_data:
                self.message_user(
                    request,
                    f'Prioridad de "{obj.titulo}" cambiada a {obj.get_prioridad_display()}.'
                )


