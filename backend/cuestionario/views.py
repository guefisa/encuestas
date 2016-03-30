from django.http import HttpResponse
from django.template import loader
from rest_framework import generics

from .models import Pregunta
from .serializers import PreguntaSerializer

'''
Estas clases genericas contruyen nuestra API y
nos proporcionan una interfaz web para navegar por ella.
'''
class PreguntaList(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class PreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer