from rest_framework import serializers

from .models import Pregunta, Opcion


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('pk', 'pregunta', 'texto', 'valor', 'salto', 'orden')

# Serializamos las opciones dentro de las preguntas
class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ('pk', 'codigo', 'texto', 'opciones', 'opcion_seleccionada', 'salto', 'orden',)