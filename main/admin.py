# django imports
from django.contrib import admin

# local imports
from main.models import BlogEntry, ProjectEntry


class BlogEntryAdmin(admin.ModelAdmin):
    ordering = ('-display_date',)
    readonly_fields = ('created', 'modified')


admin.site.register(BlogEntry, BlogEntryAdmin)


class ProjectEntryAdmin(admin.ModelAdmin):
    ordering = ('-display_date',)
    readonly_fields = ('created', 'modified')


admin.site.register(ProjectEntry, ProjectEntryAdmin)
