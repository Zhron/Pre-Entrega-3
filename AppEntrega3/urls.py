"""
URL configuration for Clases_Coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppEntrega3 import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About")
]

# Cursos
urlpatterns += [
    path('curso-list/', views.CursoListView.as_view(), name="CursoList"),
    path('curso-detail/<int:pk>/', views.CursoDetailView.as_view(), name="CursoDetail"),
    path('curso-create/', views.CursoCreateView.as_view(), name="CursoCreate"),
    path('curso-update/<int:pk>/', views.CursoUpdateView.as_view(), name="CursoUpdate"),
    path('curso-delete/<int:pk>/', views.CursoDeleteView.as_view(), name="CursoDelete"),
]

# Estudiantes
urlpatterns += [
    path('estudiante-list/', views.EstudianteListView.as_view(), name="EstudianteList"),
    path('estudiante-detail/<int:pk>/', views.EstudianteDetailView.as_view(), name="EstudianteDetail"),
    path('estudiante-create/', views.EstudianteCreateView.as_view(), name="EstudianteCreate"),
    path('estudiante-update/<int:pk>/', views.EstudianteUpdateView.as_view(), name="EstudianteUpdate"),
    path('estudiante-delete/<int:pk>/', views.EstudianteDeleteView.as_view(), name="EstudianteDelete"),
]

# Profesores
urlpatterns += [
    path('profesor-list/', views.ProfesorListView.as_view(), name="ProfesorList"),
    path('profesor-detail/<int:pk>/', views.ProfesorDetailView.as_view(), name="ProfesorDetail"),
    path('profesor-create/', views.ProfesorCreateView.as_view(), name="ProfesorCreate"),
    path('profesor-update/<int:pk>/', views.ProfesorUpdateView.as_view(), name="ProfesorUpdate"),
    path('profesor-delete/<int:pk>/', views.ProfesorDeleteView.as_view(), name="ProfesorDelete"),
]

# Busqueda de Camadas
urlpatterns += [
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
]