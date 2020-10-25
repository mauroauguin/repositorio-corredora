from django.db import models
from django.utils import timezone

class Propietario(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	nombre = models.CharField('Nombre', max_length = 100)
	apellido = models.CharField('Apellido', max_length = 100)
	telefono = models.CharField('Telefono', max_length = 13)
	email = models.EmailField('Email')
	fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add =False)

	class Meta:
		verbose_name = 'Propietario'
		verbose_name_plural = 'Propietarios'
		ordering = ['nombre']


	def __str__(self):
		return self.nombre

class Arrendatario(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	nombre = models.CharField('Nombre', max_length = 100)
	apellido = models.CharField('Apellido', max_length = 100)
	telefono = models.CharField('Telefono', max_length = 13)
	email = models.EmailField('Email')
	fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add =False)

	class Meta:
		verbose_name = 'Arrendatario'
		verbose_name_plural = 'Arrendatarios'
		ordering = ['nombre']


	def __str__(self):
		return self.nombre



class Propiedad(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, blank=True, null=True)
	direccion = models.CharField('Dirección', max_length = 100)
	comuna = models.CharField('Comuna', max_length = 100)
	region = models.CharField('Region', max_length = 100)
	dormitorios = models.PositiveIntegerField(default=0)
	baños = models.PositiveIntegerField(default=0)
	estacionamiento = models.PositiveIntegerField(default=0)
	bodega = models.PositiveIntegerField(default=0)
	pisos = models.PositiveIntegerField(default=0)
	huespedes = models.PositiveIntegerField(default=0)
	gasto_comun = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	tipo = models.BooleanField()
	fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add =False)

	class Meta:
		verbose_name = 'Propiedad'
		verbose_name_plural = 'Propiedades'
		ordering = ['direccion']


	def __str__(self):
		return self.direccion


class Arriendo(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	arrendatario = models.ForeignKey(Arrendatario, on_delete=models.CASCADE)
	propiedad = models.OneToOneField(Propiedad, on_delete=models.CASCADE)
	fecha_inicio = models.DateTimeField(blank=True, null=True)
	fecha_termino = models.DateTimeField(blank=True, null=True)
	precio = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	monto_reserva = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	comentario = models.TextField(blank=True, null = True)
	garantia = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	evaluacion = models.CharField('Evaluación', max_length = 20, blank=True, null = True)
	descuento = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	saldo_pendiente = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	multa = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	comision = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null = True)
	trato = models.CharField('Trato', max_length = 20, blank=True, null = True)
	dia_pago = models.DateField(blank=True, null=True)
	fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add =False)

	class Meta:
		verbose_name = 'Arriendo'
		verbose_name_plural = 'Arriendos'
		ordering = ['fecha_creacion']


	def __str__(self):
		return str(self.propiedad)
