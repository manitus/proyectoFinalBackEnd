from django.db import models


class Tarea(models.Model):
    titulo=models.CharField(max_length=100, verbose_name='titulo')
    # puede quedar vacío este campo, puede quedar nulo
    categoria=models.CharField(max_length=50, verbose_name='categoria', null=True)
    descripcion=models.CharField(max_length=200, verbose_name='descripcion')
    fecha_fin=models.DateField(verbose_name='fecha de fin')
# datefield tiene solo fecha, sin hora

    def __str__(self):
        return f'{self.titulo} - ({self.categoria}) ({self.fecha_fin})'
