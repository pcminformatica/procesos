from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from decimal import Decimal

#Almacena los diferentes del sistema activo, inactivo, oculto o eliminado
class EstadoSistemas(models.Model):
	codigo =  models.CharField(max_length=30)
	nombre =  models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actulización")
	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.nombre

class EstadoAcciones(models.Model):
	codigo =  models.CharField(max_length=30)
	nombre =  models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actulización")
	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.nombre

class PlanAcciones(models.Model):
	titulo =  models.CharField(max_length=250)
	ninforme =  models.CharField(max_length=250)
	periodo =  models.CharField(max_length=250)
	fecha  = models.DateField()
	estadosistema =  models.ForeignKey('proyectos.EstadoSistemas',related_name='planesacciones_estadosistema', blank=True, null=True,on_delete=models.CASCADE) 
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actulización")
	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.titulo

class Acciones(models.Model):
	titulo = models.TextField()
	recomendacion = models.TextField()
	respoejecucion = models.TextField()
	actividadrealizar = models.TextField()
	fechaejecucion = models.DateField()
	firmaresponsable = models.TextField()
	observacion = models.TextField()
	plan =  models.ForeignKey('proyectos.PlanAcciones',related_name='acciones_estadosistema', blank=True, null=True,on_delete=models.CASCADE) 
	estadoacciones =  models.ForeignKey('proyectos.EstadoAcciones',related_name='estado_estadosistema', blank=True, null=True,on_delete=models.CASCADE) 
	estadosistema =  models.ForeignKey('proyectos.EstadoSistemas',related_name='acciones_estadosistema', blank=True, null=True,on_delete=models.CASCADE) 
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actulización")
	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.recomendacion