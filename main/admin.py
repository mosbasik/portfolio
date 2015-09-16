# django imports
from django.contrib import admin

# local imports
from main.models import Entry


class EntryAdmin(admin.ModelAdmin):
    ordering = ('-display_date',)
    readonly_fields = ('created', 'modified')


admin.site.register(Entry, EntryAdmin)
