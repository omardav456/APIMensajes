from django.shortcuts import render
from rest_framework import viewsets
from .models import Notificacion
from .serializers import NotificacionSerializer
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class NotificacionViewSet(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all().order_by('-fecha_creacion')

    def get_queryset(self):
        # Mostrar solo las notificaciones activas
        return Notificacion.objects.all().order_by('-fecha_creacion')

    def eliminar_notificaciones_viejas(self):
        """ Eliminar las notificaciones que tienen más de 15 minutos. """
        expiracion = timezone.now() - timedelta(minutes=15)
        Notificacion.objects.filter(fecha_creacion__lt=expiracion).delete()

    @action(detail=False, methods=['get'])
    def eliminar_viejas(self, request):
        """ Acción para eliminar notificaciones viejas manualmente """
        self.eliminar_notificaciones_viejas()
        return Response({"message": "Notificaciones viejas eliminadas correctamente."})