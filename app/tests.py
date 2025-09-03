from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from app.models import Task


class TaskModelTest(TestCase):
    """Tests para el modelo Task"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.task = Task.objects.create(
            titulo="Test Task",
            descripcion="Descripción de prueba",
            prioridad="alta",
            estado="pendiente",
            fecha_limite=timezone.now() + timedelta(days=1)
        )
    
    def test_task_creation(self):
        """Test: Crear una tarea"""
        self.assertEqual(self.task.titulo, "Test Task")
        self.assertEqual(self.task.prioridad, "alta")
        self.assertEqual(self.task.estado, "pendiente")
        self.assertTrue(self.task.fecha_creacion)
    
    def test_task_str_representation(self):
        """Test: Representación string de la tarea"""
        self.assertIn("Test Task", str(self.task))
    
    def test_task_esta_vencida(self):
        """Test: Verificar si una tarea está vencida"""
        # Tarea futura no debe estar vencida
        self.assertFalse(self.task.esta_vencida)
        
        # Tarea pasada debe estar vencida
        task_vencida = Task.objects.create(
            titulo="Tarea Vencida",
            prioridad="media",
            estado="pendiente",
            fecha_limite=timezone.now() - timedelta(days=1)
        )
        self.assertTrue(task_vencida.esta_vencida)
    
    def test_task_dias_restantes(self):
        """Test: Calcular días restantes"""
        task_futura = Task.objects.create(
            titulo="Tarea Futura",
            prioridad="baja",
            estado="pendiente",
            fecha_limite=timezone.now() + timedelta(days=5)
        )
        # Verificar que los días restantes son aproximadamente 5
        self.assertGreaterEqual(task_futura.dias_restantes, 4)
        self.assertLessEqual(task_futura.dias_restantes, 5)


class TaskViewsTest(TestCase):
    """Tests para las vistas de Task"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.client = Client()
        self.task = Task.objects.create(
            titulo="Tarea de Prueba",
            descripcion="Descripción de prueba",
            prioridad="alta",
            estado="pendiente",
            fecha_limite=timezone.now() + timedelta(days=1)
        )
    
    def test_dashboard_view(self):
        """Test: Vista del dashboard"""
        response = self.client.get(reverse('app:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dashboard")
    
    def test_task_list_view(self):
        """Test: Vista de lista de tareas"""
        response = self.client.get(reverse('app:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista de Tareas")
        self.assertContains(response, self.task.titulo)
    
    def test_task_detail_view(self):
        """Test: Vista de detalle de tarea"""
        response = self.client.get(reverse('app:task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.titulo)
    
    def test_task_create_view(self):
        """Test: Vista de creación de tarea"""
        response = self.client.get(reverse('app:task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nueva Tarea")
    
    def test_task_create_post(self):
        """Test: Crear tarea via POST"""
        form_data = {
            'titulo': 'Nueva Tarea Creada',
            'descripcion': 'Descripción de la nueva tarea',
            'prioridad': 'media',
            'estado': 'pendiente',
            'fecha_limite': timezone.now() + timedelta(days=2)
        }
        response = self.client.post(reverse('app:task_create'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        
        # Verificar que la tarea fue creada
        self.assertTrue(Task.objects.filter(titulo='Nueva Tarea Creada').exists())


class TaskStatisticsTest(TestCase):
    """Tests para estadísticas del dashboard"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.client = Client()
        
        # Crear tareas con diferentes estados para estadísticas
        Task.objects.create(
            titulo="Pendiente 1",
            prioridad="alta",
            estado="pendiente",
            fecha_limite=timezone.now() + timedelta(days=1)
        )
        
        Task.objects.create(
            titulo="Pendiente 2",
            prioridad="media",
            estado="pendiente",
            fecha_limite=timezone.now() + timedelta(days=2)
        )
        
        Task.objects.create(
            titulo="Completada 1",
            prioridad="baja",
            estado="completada",
            fecha_limite=timezone.now() + timedelta(days=3)
        )
        
        Task.objects.create(
            titulo="En Progreso 1",
            prioridad="urgente",
            estado="en_progreso",
            fecha_limite=timezone.now() + timedelta(days=4)
        )
    
    def test_dashboard_statistics(self):
        """Test: Verificar estadísticas en el dashboard"""
        response = self.client.get(reverse('app:dashboard'))
        self.assertEqual(response.status_code, 200)
        
        # Verificar que las estadísticas están presentes
        self.assertContains(response, "Pendientes")
        self.assertContains(response, "Completadas")
        self.assertContains(response, "En Progreso")
    
    def test_task_count_by_status(self):
        """Test: Contar tareas por estado"""
        pendientes = Task.objects.filter(estado='pendiente').count()
        completadas = Task.objects.filter(estado='completada').count()
        en_progreso = Task.objects.filter(estado='en_progreso').count()
        
        self.assertEqual(pendientes, 2)
        self.assertEqual(completadas, 1)
        self.assertEqual(en_progreso, 1)
    
    def test_task_count_by_priority(self):
        """Test: Contar tareas por prioridad"""
        urgentes = Task.objects.filter(prioridad='urgente').count()
        altas = Task.objects.filter(prioridad='alta').count()
        medias = Task.objects.filter(prioridad='media').count()
        bajas = Task.objects.filter(prioridad='baja').count()
        
        self.assertEqual(urgentes, 1)
        self.assertEqual(altas, 1)
        self.assertEqual(medias, 1)
        self.assertEqual(bajas, 1)