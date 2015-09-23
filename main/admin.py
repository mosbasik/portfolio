# django imports
from django.contrib import admin

# local imports
from main.models import TextBlock, Blog, Project, LocalFile


class TextBlockAdmin(admin.ModelAdmin):
    ordering = ('name',)
    readonly_fields = ('created', 'modified')
    fields = ('created', 'modified', 'name', 'body')


admin.site.register(TextBlock, TextBlockAdmin)


class BlogAdmin(admin.ModelAdmin):
    ordering = ('-display_date',)
    readonly_fields = ('created', 'modified', 'slug', 'url')


admin.site.register(Blog, BlogAdmin)


class ProjectAdmin(admin.ModelAdmin):
    ordering = ('-display_date',)
    readonly_fields = ('created', 'modified', 'slug', 'url')


admin.site.register(Project, ProjectAdmin)


admin.site.register(LocalFile)
