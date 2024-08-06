from django.shortcuts import render
from .models import Curso
from AppEntrega3.forms import CursoFormulario, BuscaCursoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Profesor
from django.urls import reverse_lazy
from django.http import HttpResponse



def inicio(request):

    return render(request, "AppEntrega3/index.html")

def busquedaCamada(request):
    return render(request, "AppEntrega3/busquedaCamada.html")

def buscar(request):
    # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"

    if request.GET["camada"]:
        
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, "AppEntrega3/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    
    else:
        
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def about(request):
    return render(request, "AppEntrega3/about.html")



class CursoListView(ListView):
    model = Curso
    template_name = "AppEntrega3/curso_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppEntrega3/curso_detail.html"


class CursoCreateView(CreateView):


    model = Curso
    template_name = "AppEntrega3/curso_create.html"
    fields = ["nombre", "camada"]

    success_url = reverse_lazy("CursoList")


class CursoUpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    fields = ["nombre", "camada"]
    template_name = "AppEntrega3/curso_update.html"


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = 'AppEntrega3/curso_confirm_delete.html'



class EstudianteListView(ListView):
    model = Estudiante
    template_name = "AppEntrega3/estudiante_list.html"


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "AppEntrega3/estudiante_detail.html"


class EstudianteCreateView(CreateView):

    model = Estudiante
    template_name = "AppEntrega3/estudiante_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("EstudianteList")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppEntrega3/estudiante_update.html"


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = 'AppEntrega3/estudiante_confirm_delete.html'



class ProfesorListView(ListView):
    model = Profesor
    template_name = "AppEntrega3/profesor_list.html"


class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "AppEntrega3/profesor_detail.html"


class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = "AppEntrega3/profesor_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("ProfesorList")


class ProfesorUpdateView(UpdateView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppEntrega3/profesor_update.html"


class ProfesorDeleteView(DeleteView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    template_name = 'AppEntrega3/profesor_confirm_delete.html'