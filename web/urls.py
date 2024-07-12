from django.urls import path
from . import views  # el punto es xq importamos del mismo directorio, y lo q importamos

# es la view q hicimos

urlpatterns = [
    path('', views.index, name='index'),  # acá registro la url para asociar vista y url
    path('lista', views.TareasListView.as_view(), name='tareas_listado'),
    path('crear', views.TareasCreateView.as_view(), name='tareas_crear'),
    path('detalle/<pk>', views.TareasDetailView.as_view(), name='tareas_detalle_receta'),
    path('modificar/<pk>', views.TareasUpdateView.as_view(), name='tareas_modificar'),
    path('borrar/<pk>', views.TareasDeleteView.as_view(), name='tareas_borrar'),
    # ej de pag parametrizada
    path('saludar/<str:nombre_usuario>', views.saludar_por_nombre, name='saludar_por_nombre')
]
