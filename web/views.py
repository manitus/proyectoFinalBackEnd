from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

from .models import Tarea


# Create your views here.

def index(request):  #request es lo q me pida el browser

    context = {
        'username': 'Juanca',
        'fecha_hoy': datetime.now(),

    }
    return render(request, 'web/index.html', context)


def crear_tarea(request):
    return HttpResponse('trabajo en progreso. Acá se podrán dar de alta nuevas tareas')


#tareas_listado queda sin acceso
# def tareas_listado(request):
#     #esta lista está hardcodeada, luego se logrará obtener la listra de una DB real
#     lista_de_tareas=Tarea.objects.all()

#     context={
#         'listado_tareas': lista_de_tareas,
#         'usuario_activo': True
#     }
#     return render(request,'web/tareas_listado.html', context)

def saludar_por_nombre(request, nombre_usuario):
    return HttpResponse(f'Bienvenid@ <b>{nombre_usuario}<b>')


#vistas basadas en clases

class TareasListView(ListView):
    model = Tarea
    context_object_name = 'tareas_listado'  #esta es la variable de contexto, la podemos renombrar recetas_listado, x ej. está en tareas_listado
    template_name = 'web/tareas_listado.html'  #elegimos cómo se renderiza esta vista


class TareasCreateView(CreateView):
    model = Tarea
    template_name = 'web/tareas_crear.html '
    success_url = 'lista'  #si creo correctamente el campo, me reenvía al listado!
    fields = '__all__'  #le ofrezco al usuario todos los campos a rellenar


class TareasDetailView(DetailView):
    model = Tarea
    template_name = 'web/tareas_detalle.html'


class TareasUpdateView(UpdateView):
    model = Tarea
    template_name = 'web/tareas_modificar.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('tareas_detalle_receta', kwargs={'pk': self.object.pk})


class TareasDeleteView(DeleteView):
    model = Tarea
    template_name = 'web/tareas_borrar.html'
    success_url = reverse_lazy('tareas_listado')  #acá al borrar el registro, nos envia a la lista
