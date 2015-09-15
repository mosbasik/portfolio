# django imports
from django.contrib import admin

# local imports
from main.models import Entry, Section


class SectionInline(admin.TabularInline):
    model = Section
    ordering = ('order', 'created')


class EntryAdmin(admin.ModelAdmin):
    ordering = ('-display_date',)
    readonly_fields = ('created', 'modified')
    inlines = [
        SectionInline,
    ]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Section)
