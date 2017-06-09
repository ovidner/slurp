from rest_framework import serializers

from . import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'nickname'
        )


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consumption
        fields = (
            'id',
            'timestamp',
            'person',
            'quantity',
        )


