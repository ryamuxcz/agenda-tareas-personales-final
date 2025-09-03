from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    """
    Modelo para representar una tarea personal en la agenda.
    Campos obligatorios: título, prioridad, estado, fecha límite
    """
    
    PRIORITY_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título descriptivo de la tarea"
    )
    
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='media',
        verbose_name="Prioridad",
        help_text="Nivel de prioridad de la tarea"
    )
    
    estado = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pendiente',
        verbose_name="Estado",
        help_text="Estado actual de la tarea"
    )
    
    fecha_limite = models.DateTimeField(
        verbose_name="Fecha Límite",
        help_text="Fecha y hora límite para completar la tarea"
    )
    
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Descripción detallada de la tarea (opcional)"
    )
    
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de Actualización"
    )
    
    completada_en = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Completada en",
        help_text="Fecha y hora cuando se completó la tarea"
    )
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.get_estado_display()}"
    
    def save(self, *args, **kwargs):
        # Si el estado cambia a completada, registrar la fecha
        if self.estado == 'completada' and not self.completada_en:
            self.completada_en = timezone.now()
        elif self.estado != 'completada':
            self.completada_en = None
        
        super().save(*args, **kwargs)
    
    @property
    def esta_vencida(self):
        """Verifica si la tarea está vencida"""
        if self.estado in ['completada', 'cancelada']:
            return False
        return timezone.now() > self.fecha_limite
    
    @property
    def dias_restantes(self):
        """Calcula los días restantes hasta la fecha límite"""
        if self.estado in ['completada', 'cancelada']:
            return 0
        
        delta = self.fecha_limite - timezone.now()
        return max(0, delta.days)
