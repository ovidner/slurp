from rest_framework import viewsets

from . import models, serializers


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class ConsumptionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConsumptionSerializer
    queryset = models.Consumption.objects.all()
