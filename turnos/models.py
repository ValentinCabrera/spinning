# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    tipodoc = models.ForeignKey('Tipodoc', models.DO_NOTHING, db_column='tipodoc', blank=True, null=True)
    numdoc = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)
    numtel = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='plan', blank=True, null=True)
    direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumno'


class Barrio(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey('Localidad', models.DO_NOTHING, db_column='localidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barrio'


class Bicicleta(models.Model):
    marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='marca', blank=True, null=True)
    fechacompra = models.DateField(blank=True, null=True)
    fechaultimoservice = models.DateField(blank=True, null=True)
    fechaproximoservice = models.DateField(blank=True, null=True)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bicicleta'


class Detalleturno(models.Model):
    idalumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='idalumno', blank=True, null=True)
    idturno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='idturno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleturno'


class Diasemana(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diasemana'


class Direccion(models.Model):
    calle = models.CharField(max_length=50, blank=True, null=True)
    numaltura = models.IntegerField(blank=True, null=True)
    barrio = models.ForeignKey(Barrio, models.DO_NOTHING, db_column='barrio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Garantia(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    unidadmedida = models.ForeignKey('Unidadmedida', models.DO_NOTHING, db_column='unidadmedida', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garantia'


class Horario(models.Model):
    horainicio = models.TimeField(blank=True, null=True)
    horafin = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Localidad(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    codpostal = models.IntegerField(blank=True, null=True)
    provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidad'


class Marca(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'


class Modelo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    garantia = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelo'


class Pais(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Plan(models.Model):
    cantidaddias = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class Profesor(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    tipodoc = models.ForeignKey('Tipodoc', models.DO_NOTHING, db_column='tipodoc', blank=True, null=True)
    numdoc = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'


class Proveedor(models.Model):
    razonsocial = models.CharField(max_length=50, blank=True, null=True)
    cuit = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    numtel = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Provincia(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Tipodoc(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodoc'


class Turno(models.Model):
    horario = models.ForeignKey(Horario, models.DO_NOTHING, db_column='horario', blank=True, null=True)
    diasemana = models.ForeignKey(Diasemana, models.DO_NOTHING, db_column='diasemana', blank=True, null=True)
    capacidadmax = models.IntegerField(blank=True, null=True)
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='profesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turno'


class TurnoBicicleta(models.Model):
    idturno = models.ForeignKey(Turno, models.DO_NOTHING, db_column='idturno', blank=True, null=True)
    idbicicleta = models.ForeignKey(Bicicleta, models.DO_NOTHING, db_column='idbicicleta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turno_bicicleta'


class Unidadmedida(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidadmedida'
