from django.contrib import admin
from django.db.models import ManyToManyField

from .models import Insulation, Variety


# Register your models here.


@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sheet_area', 'sheet_volume', 'sheets_package')
    list_display_links = ('title', 'sheet_area', 'sheet_volume', 'sheets_package',)
    search_fields = ('title', 'sheet_area', 'sheet_volume', 'sheets_package',)
    list_filter = ('title', 'sheet_area', 'sheet_volume', 'sheets_package',)
    readonly_fields = ('created', 'updated',)


@admin.register(Insulation)
class InsulationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        ManyToManyField
    )
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    readonly_fields = ('created', 'updated',)

