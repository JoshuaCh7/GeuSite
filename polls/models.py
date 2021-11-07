import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
# Create your models here.
from GEUsite import settings

#
# class tipoUsuario(models.Model):
#     idTipoUsuario = models.AutoField(primary_key=True)
#     tipoUsuario = models.CharField(max_length=20, null=False, blank=False)
#     estado = models.BooleanField(default=True)

# class perfil(models.Model):
#     #fkGroup = models.OneToOneField(Group, on_delete= models.PROTECT)
#     fkTipoUsuario= models.OneToOneField(tipoUsuario,on_delete=models.PROTECT, null=False,
#                                       related_name='tipoUsuario_usuario')
#     fkUsuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=False,
#                                       related_name='usuario_TipoUsuario')
#     estado = models.BooleanField(default=True)
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    content= models.TextField()
    def __str__(self):
        return self.title

class modulo(models.Model):
    idModulo = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombreModulo = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)


class tipoLeccion(models.Model):
    idTipoLeccion = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tipoLeccion = models.CharField(max_length=20, null=False, blank=False)
    estado = models.BooleanField(default=True)

class respuesta(models.Model):
    idRespuesta = models.UUIDField(primary_key=True, default=uuid.uuid4)
    fkUsuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                  related_name='respuesta_usuario')
    respuesta = models.CharField(max_length=200, null=False, blank=False)
    estado = models.CharField(max_length=100, null=False, blank=False)

class leccion(models.Model):
    fkTipoLeccion = models.ForeignKey(tipoLeccion, on_delete=models.PROTECT)
    fkRespuesta = models.ForeignKey(respuesta, on_delete=models.PROTECT)
    idLeccion = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombreLeccion = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)

class archivos(models.Model):
    fkUsuarioCreacion = models.ForeignKey(User, on_delete=models.PROTECT,
                                          related_name='archivos_usuario_creacion')
    idArchivo = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombreArchivo = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    archivo = models.FileField()
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaEdicion = models.DateTimeField(auto_now_add=True)