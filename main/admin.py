# django imports
from django.contrib import admin

# local imports
from main.models import Entry, Section



class SectionInline(admin.TabularInline):
    model = Section


class EntryAdmin(admin.ModelAdmin):
    inlines = [
        SectionInline,
    ]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Section)
