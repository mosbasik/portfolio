# django imports
from django.core.management.base import BaseCommand, CommandError

# local imports
from main.models import Blog, Project

# python imports
from dateutil import parser
import json


class Command(BaseCommand):
    help = 'Loads sample data into the database for testing.'

    def handle(self, *args, **options):

        Blog.objects.all().delete()
        Project.objects.all().delete()

        with open('main/management/commands/sample_data.json', 'r') as f:
            data = json.load(f)

            for i, entry in enumerate(data):

                if i > 10:
                    break

                print "Loading entry {}: {}".format(i, entry['entry_title'])

                if entry['kind'] == 'Blog':
                    new_entry = Blog(
                        title=entry['entry_title'],
                        display_date=parser.parse(entry['date']),
                        body=entry['section_1'],
                    )
                    new_entry.save()
                else:
                    new_entry = Project(
                        title=entry['entry_title'],
                        display_date=parser.parse(entry['date']),
                        body=entry['section_1'],
                    )
                    new_entry.save()
