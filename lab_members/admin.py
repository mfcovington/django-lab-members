from django.contrib import admin
from lab_members.models import Position, Scientist, Institution, Degree, Field, Advisor, Education, Employment

class PositionAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Position, PositionAdmin)


class EducationInline(admin.TabularInline):
    model = Education
    extra = 3


class EmploymentInline(admin.TabularInline):
    model = Employment
    extra = 3


class ScientistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['full_name', 'title']}),
        ('Bio',        {'fields': ['personal_interests', 'research_interests']}),
        ('Advanced',   {'fields': ['slug'], 'classes': ['collapse']}),
    ]

    inlines = [EducationInline, EmploymentInline]

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


class AdvisorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advisor, AdvisorAdmin)

admin.site.site_header = 'Lab Member Administration'
