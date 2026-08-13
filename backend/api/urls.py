from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informacion/', views.about, name='about'),
    path('perfil/', views.profile_view, name='profile'),
    path('configuracion/', views.settings_view, name='settings'),
    path('publicar/', views.create_food, name='create_food'),
    path('alimentos/', views.lista_alimentos, name='lista_alimentos'),
]