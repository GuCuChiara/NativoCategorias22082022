from django.db import models

# Create your models here.

class codigossancor(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    Presta_Id = models.CharField(db_column='Presta_Id', primary_key=True, max_length=20, verbose_name='Código prestación Sancor')
    Descripcion = models.CharField(db_column='Descripcion', max_length=400, blank=True, null=True, verbose_name='Descripción prestación Sancor')
    cie10nativos = models.ManyToManyField('cie10nativo', through='prestaxcie10')

    def __str__(self): #método String para mostrar correcto el nombre en la BD
        return 'Codigo Prestación AMS: %s  Descripción: %s' % (self.Presta_Id, self.Descripcion)

class cie10nativo(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    CIE_10_Id = models.CharField(db_column='CIE_10_Id', primary_key=True, max_length=8, verbose_name='Código CIE 10 4 dígitos')
    CIE10_DESC = models.CharField(db_column='CIE10_DESC', max_length=400, blank=True, null=True, verbose_name='Descripción CIE 10')
    codigossancors = models.ManyToManyField('codigossancor', through='prestaxcie10')

    def __str__(self):
        return 'CIE 10 ID: %s CIE10 Descripción: %s ' % (self.CIE_10_Id, self.CIE10_DESC)

class prestaxcie10(models.Model):
    id = models.BigIntegerField(primary_key=True)
    prestacion_Id = models.ForeignKey(codigossancor, on_delete=models.CASCADE, null=True)
    codCIE10_Id = models.ForeignKey(cie10nativo, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return '%s %s' % (self.prestacion_Id , self.codCIE10_Id)