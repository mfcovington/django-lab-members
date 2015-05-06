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
    fieldset_basic = ('Basic Info', {
        'fields': [
            'full_name',
            'email',
            'title',
            'photo',
            'current',
            'alumni_redirect_url',
            'visible',
        ]
    })

    fieldset_website = ('Website', {
        'fields': [
            'website_url',
            'website_name',
        ],
    })

    fieldset_bio = ('Bio', {
        'fields': [
            'personal_interests',
            'research_interests',
        ],
    })

    fieldset_advanced = ('Advanced', {
        'fields': ['slug'],
        'classes': ['collapse'],
    })

    fieldsets = [
        fieldset_basic,
        fieldset_website,
        fieldset_bio,
        fieldset_advanced,
    ]

    inlines = [EducationInline, EmploymentInline]

    list_display = ['full_name', 'title', 'email', 'current', 'visible']
    list_filter = ['title', 'current', 'visible']
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
