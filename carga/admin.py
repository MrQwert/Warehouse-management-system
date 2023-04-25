from django.contrib import admin
from .models import CSV

@admin.register(CSV)
class CSVAdmin(admin.ModelAdmin):
    pass

