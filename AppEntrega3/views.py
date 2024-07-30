from django.shortcuts import render
from .models import Curso
from AppEntrega3.forms import CursoFormulario, BuscaCursoForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Profesor
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin


# Dejamos la vista INICIO basada en funciones y visible para todos
def inicio(request):
    # imagen = Imagen.objects.filter(user=request.user.id)[0]
    # print(imagen)
    return render(request, "AppEntrega3/index.html")# , {"url": imagen})


# Dejamos una vista basada en funciones que requiere login para mostrar el uso de @login_required
@login_required
def about(request):
    return render(request, "AppEntrega3/about.html")


# VISTAS BASADAS EN CLASES - CURSOS
class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppEntrega3/curso_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppEntrega3/curso_detail.html"

    # login_url = '/users/login/'

    # def get_login_url(self):
    #     return self.login_url


class CursoCreateView(LoginRequiredMixin, CreateView):


    model = Curso
    template_name = "AppEntrega3/curso_create.html"
    fields = ["nombre", "camada"]

    success_url = reverse_lazy("CursoList")


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    fields = ["nombre", "camada"]
    template_name = "AppEntrega3/curso_update.html"


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = 'AppEntrega3/curso_confirm_delete.html'



class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "AppEntrega3/estudiante_list.html"


class EstudianteDetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "AppEntrega3/estudiante_detail.html"


class EstudianteCreateView(LoginRequiredMixin, CreateView):

    model = Estudiante
    template_name = "AppEntrega3/estudiante_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("EstudianteList")


class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppEntrega3/estudiante_update.html"


class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = 'AppEntrega3/estudiante_confirm_delete.html'



class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "AppEntrega3/profesor_list.html"


class ProfesorDetailView(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name = "AppEntrega3/profesor_detail.html"


class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    template_name = "AppEntrega3/profesor_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("ProfesorList")


class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppEntrega3/profesor_update.html"


class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    template_name = 'AppEntrega3/profesor_confirm_delete.html'
