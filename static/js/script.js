// Custom JavaScript for Agenda de Tareas Personales

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Toggle status functionality
    document.querySelectorAll('.toggle-status').forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.dataset.taskId;
            const button = this;
            
            // Show loading state
            button.disabled = true;
            button.innerHTML = '<i class="bi bi-hourglass-split"></i>';
            
            fetch(`/tareas/${taskId}/toggle-status/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Show success message
                    showNotification('Estado actualizado correctamente', 'success');
                    // Reload page after a short delay
                    setTimeout(() => {
                        location.reload();
                    }, 1000);
                } else {
                    showNotification('Error al actualizar el estado', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Error de conexión', 'error');
            })
            .finally(() => {
                // Restore button state
                button.disabled = false;
                button.innerHTML = '<i class="bi bi-arrow-clockwise"></i>';
            });
        });
    });

    // Search functionality with debounce
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                // Auto-submit form after 500ms of no typing
                const form = this.closest('form');
                if (form) {
                    form.submit();
                }
            }, 500);
        });
    }

    // Priority color coding
    document.querySelectorAll('.badge').forEach(badge => {
        const text = badge.textContent.toLowerCase();
        if (text.includes('urgente')) {
            badge.classList.add('bg-danger');
        } else if (text.includes('alta')) {
            badge.classList.add('bg-warning');
        } else if (text.includes('media')) {
            badge.classList.add('bg-info');
        } else if (text.includes('baja')) {
            badge.classList.add('bg-secondary');
        }
    });

    // Status color coding
    document.querySelectorAll('.badge').forEach(badge => {
        const text = badge.textContent.toLowerCase();
        if (text.includes('completada')) {
            badge.classList.add('bg-success');
        } else if (text.includes('en progreso')) {
            badge.classList.add('bg-primary');
        } else if (text.includes('pendiente')) {
            badge.classList.add('bg-warning');
        } else if (text.includes('cancelada')) {
            badge.classList.add('bg-secondary');
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    });

    cards.forEach(card => {
        observer.observe(card);
    });
});

// Utility functions
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    
    notification.innerHTML = `
        <i class="bi bi-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-triangle' : 'info-circle'} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 3 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 3000);
}

// Date formatting helper
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Priority level helper
function getPriorityLevel(priority) {
    const levels = {
        'urgente': 4,
        'alta': 3,
        'media': 2,
        'baja': 1
    };
    return levels[priority] || 0;
}

// Status level helper
function getStatusLevel(status) {
    const levels = {
        'completada': 4,
        'en_progreso': 3,
        'pendiente': 2,
        'cancelada': 1
    };
    return levels[status] || 0;
}

// Export functions for use in other scripts
window.TaskManager = {
    showNotification,
    formatDate,
    getPriorityLevel,
    getStatusLevel
};