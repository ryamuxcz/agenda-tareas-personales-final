from django import forms
from django.utils import timezone
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Formulario para crear y editar tareas.
    Incluye validaciones personalizadas y widgets mejorados.
    """
    
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'prioridad', 'estado', 'fecha_limite']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el título de la tarea',
                'maxlength': '200'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción detallada de la tarea (opcional)',
                'rows': 4
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_limite': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }
        labels = {
            'titulo': 'Título de la Tarea',
            'descripcion': 'Descripción',
            'prioridad': 'Prioridad',
            'estado': 'Estado',
            'fecha_limite': 'Fecha Límite'
        }
        help_texts = {
            'titulo': 'Título descriptivo y claro de la tarea',
            'descripcion': 'Información adicional sobre la tarea (opcional)',
            'prioridad': 'Nivel de importancia de la tarea',
            'estado': 'Estado actual de la tarea',
            'fecha_limite': 'Fecha y hora límite para completar la tarea'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Establecer fecha mínima como ahora
        now = timezone.now()
        self.fields['fecha_limite'].widget.attrs['min'] = now.strftime('%Y-%m-%dT%H:%M')
        
        # Si es una edición, permitir fechas pasadas
        if self.instance.pk:
            self.fields['fecha_limite'].widget.attrs.pop('min', None)
    
    def clean_titulo(self):
        """
        Validación personalizada para el título.
        """
        titulo = self.cleaned_data.get('titulo')
        if titulo:
            titulo = titulo.strip()
            if len(titulo) < 3:
                raise forms.ValidationError(
                    'El título debe tener al menos 3 caracteres.'
                )
            if len(titulo) > 200:
                raise forms.ValidationError(
                    'El título no puede exceder 200 caracteres.'
                )
        return titulo
    
    def clean_fecha_limite(self):
        """
        Validación personalizada para la fecha límite.
        """
        fecha_limite = self.cleaned_data.get('fecha_limite')
        if fecha_limite:
            now = timezone.now()
            
            # Si es una nueva tarea, la fecha límite debe ser futura
            if not self.instance.pk and fecha_limite <= now:
                raise forms.ValidationError(
                    'La fecha límite debe ser una fecha futura para nuevas tareas.'
                )
            
            # Si es una edición, permitir fechas pasadas pero mostrar advertencia
            if self.instance.pk and fecha_limite <= now:
                # Solo mostrar advertencia si el estado no es completada o cancelada
                if self.cleaned_data.get('estado') not in ['completada', 'cancelada']:
                    # No lanzar error, solo registrar advertencia
                    pass
        
        return fecha_limite
    
    def clean(self):
        """
        Validaciones que involucran múltiples campos.
        """
        cleaned_data = super().clean()
        estado = cleaned_data.get('estado')
        fecha_limite = cleaned_data.get('fecha_limite')
        
        # Si la tarea está completada, verificar que tenga fecha límite
        if estado == 'completada' and not fecha_limite:
            raise forms.ValidationError(
                'Las tareas completadas deben tener una fecha límite establecida.'
            )
        
        return cleaned_data


class TaskFilterForm(forms.Form):
    """
    Formulario para filtrar tareas en la lista.
    """
    ESTADO_CHOICES = [('', 'Todos los estados')] + Task.STATUS_CHOICES
    PRIORIDAD_CHOICES = [('', 'Todas las prioridades')] + Task.PRIORITY_CHOICES
    
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título o descripción...',
            'maxlength': '100'
        }),
        label='Buscar'
    )
    
    estado = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Estado'
    )
    
    prioridad = forms.ChoiceField(
        choices=PRIORIDAD_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Prioridad'
    )


