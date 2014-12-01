from django.contrib import admin
from lab_members.models import Position, Scientist, Institution, Degree, Field, Education

class PositionAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Position, PositionAdmin)


class EducationInline(admin.TabularInline):
    model = Education
    extra = 3


class ScientistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['full_name', 'title']}),
        ('Bio',        {'fields': ['personal_interests', 'research_interests']}),
        ('Advanced',   {'fields': ['slug'], 'classes': ['collapse']}),
    ]

    inlines = [EducationInline]

    list_display = ['full_name', 'title']
    list_filter = ['title']
    search_fields = ['full_name']

    prepopulated_fields = {"slug": ("full_name",)}

admin.site.register(Scientist, ScientistAdmin)


class InstitutionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Institution, InstitutionAdmin)


class DegreeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Degree, DegreeAdmin)


class FieldAdmin(admin.ModelAdmin):
    pass

admin.site.register(Field, FieldAdmin)

admin.site.site_header = 'Lab Member Administration'
