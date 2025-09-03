from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = 'Agenda de Tareas Personales'
    
    def ready(self):
        """Configuración inicial de la aplicación."""
        # Importar señales si las hay
        # import app.signals
        pass


