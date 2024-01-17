from django.contrib import admin
from .models import Insulation


# Register your models here.


@admin.register(Insulation)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sheet_area', 'sheet_volume', 'sheets_package')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('sheets_package',)
    readonly_fields = ('created', 'updated',)
