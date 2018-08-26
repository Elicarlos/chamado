from django.contrib import admin
from .models import Cliente, Chamado, Tecnico

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Chamado)
admin.site.register(Tecnico)
