from django.contrib import admin
import search.models as sm


@admin.register(sm.Car)
class AlertConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'year')
