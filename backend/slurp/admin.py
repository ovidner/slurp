from django.contrib import admin

from . import models

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    pass
