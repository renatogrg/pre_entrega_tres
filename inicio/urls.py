from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_inicio, name='inicio'),
    path('crear-animal/', views.crear_carro, name='crear_carro'),
    path('animales/', views.lista_carros, name='listar_carros'),
    
]