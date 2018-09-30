from django.contrib import admin
from engines.models import Engine

# Register your models here.
class EngineAdmin(admin.ModelAdmin):
    list_display = ['pojemnosc', 'id', 'ilosc_cylindrow', 'rodzaj']
    search_fields = ['pojemnosc']
    list_filter = ['rodzaj']

admin.site.register(Engine, EngineAdmin)