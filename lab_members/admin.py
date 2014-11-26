from django.contrib import admin
from lab_members.models import Position, Scientist

class PositionAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Position, PositionAdmin)

class ScientistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['full_name', 'title']}),
        ('Advanced',   {'fields': ['slug'], 'classes': ['collapse']}),
    ]

    list_display = ['full_name', 'title']
    list_filter = ['title']
    search_fields = ['full_name']

    prepopulated_fields = {"slug": ("full_name",)}

admin.site.register(Scientist, ScientistAdmin)

admin.site.site_header = 'Lab Member Administration'
