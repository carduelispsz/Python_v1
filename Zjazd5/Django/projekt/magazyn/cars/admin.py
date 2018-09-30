from django.contrib import admin
from cars.models import Car

# Register your models here.

class CarsAdmin(admin.ModelAdmin):
    list_display = ['marka', 'id', 'model', 'rok_prod', 'nadwozie', 'engine']
    search_fields = ['name']
    list_filter = ['rok_prod']

admin.site.register(Car, CarsAdmin)