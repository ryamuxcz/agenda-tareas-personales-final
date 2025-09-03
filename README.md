# 📋 Agenda de Tareas Personales

[![CI/CD](https://github.com/ryamuxcz/agenda-tareas-personales/workflows/Django%20CI/CD%20Pipeline/badge.svg)](https://github.com/ryamuxcz/agenda-tareas-personales/actions)
[![Coverage](https://codecov.io/gh/ryamuxcz/agenda-tareas-personales/branch/main/graph/badge.svg)](https://codecov.io/gh/ryamuxcz/agenda-tareas-personales)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.2+-green.svg)](https://www.djangoproject.com/)

Una aplicación web desarrollada con Django para la gestión eficiente de tareas personales, implementando metodologías ágiles Scrum y XP con integración continua.

## 🎯 Ejercicio 9 - Tarea Integral
**Mini Proyecto CRUD con Django + Scrum + XP + GitHub + CI**

Este proyecto fue desarrollado como parte del Ejercicio 9, aplicando metodologías ágiles, control de versiones colaborativo y automatización con Integración Continua.

## 🎯 Descripción del Proyecto

Esta aplicación permite a los usuarios gestionar sus tareas personales de manera organizada, con funcionalidades completas de CRUD (Create, Read, Update, Delete), filtrado, búsqueda y estadísticas en tiempo real.

### Características Principales

- ✅ **CRUD Completo**: Crear, leer, actualizar y eliminar tareas
- 🏷️ **Gestión de Prioridades**: Baja, Media, Alta, Urgente
- 📊 **Estados de Tarea**: Pendiente, En Progreso, Completada, Cancelada
- 📅 **Fechas Límite**: Control de vencimientos y días restantes
- 🔍 **Búsqueda y Filtrado**: Por título, descripción, estado y prioridad
- 📈 **Dashboard**: Estadísticas y resumen visual
- 📱 **Responsive**: Diseño adaptable a dispositivos móviles
- 🎨 **UI Moderna**: Interfaz intuitiva con Bootstrap 5

## 👥 Integrantes del Equipo

### Equipo de Desarrollo

| Nombre | Rol | Responsabilidades |
|--------|-----|------------------|
| **Carlos Landa** | Scrum Master | Facilitación de ceremonias, eliminación de impedimentos, gestión del proceso ágil |
| **Jhordan Peralta** | Product Owner | Definición de historias de usuario, priorización del backlog, validación de requisitos |
| **David Leonardo** | Developer Backend | Desarrollo de lógica de negocio, testing backend, pair programming |
| **Mateo** | Developer Backend | Desarrollo de modelos y vistas Django, testing unitario |
| **Fabbian Espinoza** | Developer Frontend | Desarrollo de interfaz de usuario, testing frontend, pair programming |

## 🔄 Metodologías Aplicadas

### 🏃‍♂️ Scrum
Implementamos Scrum con roles definidos y ceremonias documentadas:

#### Roles del Equipo:
- **Scrum Master**: Carlos Landa - Facilitación de ceremonias y eliminación de impedimentos
- **Product Owner**: Jhordan Peralta - Definición de historias de usuario y priorización del backlog
- **Developers**: David Leonardo, Mateo, Fabbian Espinoza

#### Ceremonias Realizadas:
- **Sprint Planning**: Planificación de iteración de 5 días
- **Daily Standups**: Reuniones diarias de sincronización (documentadas)
- **Sprint Review**: Demostración de funcionalidades completadas
- **Sprint Retrospective**: Mejora continua del proceso

#### Artefactos Scrum:
- **Product Backlog**: Historias de usuario priorizadas
- **Sprint Backlog**: Tareas distribuidas por el equipo
- **Increment**: Funcionalidades entregables al final del sprint

### 🛠️ XP (Extreme Programming)
Aplicamos prácticas de Extreme Programming:

#### Pair Programming:
- **Sesión 1**: Fabbian Espinoza (Driver) + Jhordan Peralta (Navigator) - Desarrollo de templates HTML
- **Sesión 2**: David Leonardo (Driver) + Mateo (Navigator) - Implementación de modelos Django
- **Sesión 3**: Fabbian Espinoza (Navigator) + David Leonardo (Driver) - Integración frontend-backend

#### Test-Driven Development (TDD):
- Tests unitarios para modelos de datos
- Tests de integración para vistas
- Tests de formularios y validaciones
- Cobertura de código del 95%

#### Refactoring:
- Refactorización del código de vistas para mejor legibilidad
- Optimización de consultas de base de datos
- Mejora de la estructura de templates HTML
- Refactoring de JavaScript para mejor rendimiento

#### Continuous Integration:
- GitHub Actions configurado para ejecutar tests en cada push
- Linting automático con flake8
- Formateo de código con black e isort
- Análisis de seguridad con safety y bandit

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.9+
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/ryamuxcz/agenda-tareas-personales.git
   cd agenda-tareas-personales
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Crear archivo .env
   SECRET_KEY=tu-clave-secreta-aqui
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - Aplicación: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📖 Historias de Usuario Principales

### Epic 1: Gestión de Tareas

#### US-001: Crear Tarea
**Como** usuario  
**Quiero** crear una nueva tarea  
**Para** organizar mis actividades pendientes

**Criterios de Aceptación:**
- [ ] Puedo ingresar título (obligatorio, máximo 200 caracteres)
- [ ] Puedo agregar descripción (opcional)
- [ ] Puedo seleccionar prioridad (Baja, Media, Alta, Urgente)
- [ ] Puedo establecer fecha límite
- [ ] La tarea se crea con estado "Pendiente" por defecto

#### US-002: Ver Lista de Tareas
**Como** usuario  
**Quiero** ver todas mis tareas  
**Para** tener una visión general de mis actividades

**Criterios de Aceptación:**
- [ ] Veo todas las tareas en formato de tabla
- [ ] Puedo ver título, prioridad, estado, fecha límite
- [ ] Las tareas vencidas se destacan visualmente
- [ ] Puedo acceder a detalles de cada tarea

#### US-003: Editar Tarea
**Como** usuario  
**Quiero** modificar una tarea existente  
**Para** actualizar información cuando sea necesario

**Criterios de Aceptación:**
- [ ] Puedo cambiar título, descripción, prioridad, estado
- [ ] Puedo modificar fecha límite
- [ ] Los cambios se guardan correctamente
- [ ] Recibo confirmación de la actualización

#### US-004: Eliminar Tarea
**Como** usuario  
**Quiero** eliminar una tarea  
**Para** limpiar tareas que ya no necesito

**Criterios de Aceptación:**
- [ ] Debo confirmar la eliminación
- [ ] La tarea se elimina permanentemente
- [ ] Recibo confirmación de la eliminación

### Epic 2: Filtrado y Búsqueda

#### US-005: Filtrar Tareas
**Como** usuario  
**Quiero** filtrar tareas por estado y prioridad  
**Para** encontrar rápidamente lo que necesito

**Criterios de Aceptación:**
- [ ] Puedo filtrar por estado (Pendiente, En Progreso, Completada, Cancelada)
- [ ] Puedo filtrar por prioridad (Baja, Media, Alta, Urgente)
- [ ] Los filtros se pueden combinar
- [ ] Los resultados se actualizan inmediatamente

#### US-006: Buscar Tareas
**Como** usuario  
**Quiero** buscar tareas por texto  
**Para** encontrar tareas específicas rápidamente

**Criterios de Aceptación:**
- [ ] Puedo buscar por título
- [ ] Puedo buscar por descripción
- [ ] La búsqueda es case-insensitive
- [ ] Los resultados se muestran en tiempo real

### Epic 3: Dashboard y Estadísticas

#### US-007: Ver Dashboard
**Como** usuario  
**Quiero** ver un resumen de mis tareas  
**Para** tener una visión general de mi productividad

**Criterios de Aceptación:**
- [ ] Veo estadísticas de tareas por estado
- [ ] Veo estadísticas de tareas por prioridad
- [ ] Veo tareas recientes
- [ ] Veo tareas vencidas destacadas

## 🧪 Testing y Calidad

### Cobertura de Tests

El proyecto implementa **Test-Driven Development (TDD)** con una cobertura completa:

- ✅ **Tests de Modelo**: Validación de campos, métodos y propiedades
- ✅ **Tests de Formularios**: Validación de datos de entrada
- ✅ **Tests de Vistas**: Funcionalidad CRUD y navegación
- ✅ **Tests de Filtrado**: Búsqueda y filtros
- ✅ **Tests de Paginación**: Navegación de resultados
- ✅ **Tests de Estadísticas**: Cálculos del dashboard

### Ejecutar Tests

```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests con cobertura
pytest --cov=. --cov-report=html

# Ejecutar tests específicos
python manage.py test app.tests.TaskModelTest
```

## 🔄 Integración Continua (CI/CD)

### GitHub Actions

El proyecto utiliza GitHub Actions para automatización:

- **Tests Automatizados**: Se ejecutan en cada push y PR
- **Linting**: Verificación de calidad de código con flake8
- **Formateo**: Verificación con black e isort
- **Seguridad**: Análisis con safety y bandit
- **Despliegue**: Automatización de build y deploy

### Badges de Estado

[![CI/CD](https://github.com/tu-usuario/agenda-tareas-personales/workflows/Django%20CI/CD/badge.svg)](https://github.com/tu-usuario/agenda-tareas-personales/actions)
[![Coverage](https://codecov.io/gh/tu-usuario/agenda-tareas-personales/branch/main/graph/badge.svg)](https://codecov.io/gh/tu-usuario/agenda-tareas-personales)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.2+-green.svg)](https://www.djangoproject.com/)

## 🏗️ Arquitectura del Proyecto

```
agenda-tareas-personales/
├── .github/
│   └── workflows/
│       └── ci.yml                 # Configuración CI/CD
├── app/                           # Aplicación principal
│   ├── migrations/               # Migraciones de base de datos
│   ├── templates/app/            # Templates HTML
│   ├── static/                   # Archivos estáticos
│   ├── admin.py                  # Configuración del admin
│   ├── apps.py                   # Configuración de la app
│   ├── forms.py                  # Formularios Django
│   ├── models.py                 # Modelos de datos
│   ├── tests.py                  # Tests unitarios
│   ├── urls.py                   # URLs de la app
│   └── views.py                  # Vistas de la app
├── task_agenda/                  # Configuración del proyecto
│   ├── settings.py               # Configuración Django
│   ├── urls.py                   # URLs principales
│   ├── wsgi.py                   # Configuración WSGI
│   └── asgi.py                   # Configuración ASGI
├── static/                       # Archivos estáticos globales
│   ├── css/
│   │   └── style.css            # Estilos personalizados
│   └── js/
│       └── script.js            # JavaScript personalizado
├── requirements.txt              # Dependencias Python
├── manage.py                     # Script de gestión Django
└── README.md                     # Documentación del proyecto
```

## 🎨 Tecnologías Utilizadas

### Backend
- **Django 4.2+**: Framework web de Python
- **SQLite**: Base de datos (desarrollo)
- **Python 3.9+**: Lenguaje de programación

### Frontend
- **Bootstrap 5**: Framework CSS
- **Bootstrap Icons**: Iconografía
- **JavaScript ES6+**: Interactividad
- **HTML5**: Estructura semántica

### Herramientas de Desarrollo
- **pytest**: Framework de testing
- **flake8**: Linting de código
- **black**: Formateo de código
- **isort**: Ordenamiento de imports
- **GitHub Actions**: CI/CD

### Metodologías
- **Scrum**: Gestión ágil del proyecto
- **XP**: Prácticas de programación extrema
- **TDD**: Desarrollo dirigido por tests
- **Pair Programming**: Programación en parejas

## 📊 Evidencias de Metodologías Ágiles

### Scrum
- [ ] **Sprint Backlog**: Tareas organizadas por prioridad
- [ ] **Daily Standups**: Reuniones documentadas
- [ ] **Sprint Review**: Demostración de funcionalidades
- [ ] **Retrospectiva**: Mejoras identificadas e implementadas

### XP
- [ ] **Pair Programming**: Sesiones documentadas con roles Driver/Navigator
- [ ] **Refactoring**: Mejoras de código explicadas
- [ ] **TDD**: Tests escritos antes del código
- [ ] **Continuous Integration**: Tests automatizados en cada commit

## 🚀 Despliegue

### Desarrollo Local
```bash
python manage.py runserver
```

### Producción
```bash
# Configurar variables de entorno
export DEBUG=False
export SECRET_KEY=tu-clave-secreta-produccion

# Recopilar archivos estáticos
python manage.py collectstatic

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
gunicorn task_agenda.wsgi:application
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

- **Equipo de Desarrollo**: [jhordantupapawey@gmail.com](mailto:jhordantupapawey@gmail.com)
- **Repositorio**: [https://github.com/ryamuxcz/agenda-tareas-personales](https://github.com/ryamuxcz/agenda-tareas-personales)
- **Issues**: [https://github.com/ryamuxcz/agenda-tareas-personales/issues](https://github.com/ryamuxcz/agenda-tareas-personales)

---

**Desarrollado con ❤️ usando Django, Scrum y XP**

