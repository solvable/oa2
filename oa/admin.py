from django.contrib import admin

from .models import Project, ProjectImages


class ProjectImagesInline(admin.StackedInline):
    model = ProjectImages
    extra = 3


class ProjectAdmin(admin.ModelAdmin):

    inlines = [ProjectImagesInline]

admin.site.register(Project, ProjectAdmin)