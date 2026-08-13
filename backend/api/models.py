from django.db import models
from django.contrib.auth.models import User

class Alimento(models.Model):
    CATEGORIAS = [
        ('Todos', 'Todos'),
        ('Frutas/Verduras', 'Frutas/Verduras'),
        ('Pan', 'Pan'),
        ('Platillos Listos', 'Platillos Listos'),
        ('Lácteos', 'Lácteos'),
        ('Carne', 'Carne'),
    ]

    titulo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=255)
    distancia = models.CharField(max_length=50)        # Ej: "1.5 km"
    horario_recogida = models.CharField(max_length=100) # Ej: "Recoger antes de las 8:00 PM hoy"
    precio = models.CharField(max_length=50, default="GRATIS")
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='Todos')
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.ubicacion}"