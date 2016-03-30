from django.db import models

'''
De momento nuestro modelo de datos sólo contempla las preguntas y sus opciones de respuesta.
'''

class Pregunta(models.Model):
    codigo = models.CharField(max_length=32, unique=True)
    texto = models.TextField(default="")
    orden = models.IntegerField(default=0)

    # Atributos temporales
    opcion_seleccionada = models.IntegerField(blank=True, null=True)
    salto = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('orden', 'pk')

    def __str__(self):
        return self.codigo


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255, default="")
    valor = models.IntegerField(default=0)
    salto = models.ForeignKey(Pregunta, blank=True, null=True)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ('orden', 'pk')

    def __str__(self):
        return self.texto