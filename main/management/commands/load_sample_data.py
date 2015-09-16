# django imports
from django.core.management.base import BaseCommand, CommandError

# local imports
from main.models import Entry

# python imports
from dateutil import parser
import json


class Command(BaseCommand):
    help = 'Loads sample data into the database for testing.'

    def handle(self, *args, **options):

        Entry.objects.all().delete()

        with open('main/management/commands/sample_data.json', 'r') as f:
            data = json.load(f)

            for i, entry in enumerate(data):

                if i > 10:
                    break

                print "Loading entry {}: {}".format(i, entry['entry_title'])
                new_entry = Entry(
                    title=entry['entry_title'],
                    kind=entry['kind'],
                    display_date=parser.parse(entry['date']),
                    body=entry['section_1'],
                )
                new_entry.save()
