from django.contrib import admin
from lab_members.models import Position, Scientist

class PositionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Position, PositionAdmin)

class ScientistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("full_name",)}

admin.site.register(Scientist, ScientistAdmin)
