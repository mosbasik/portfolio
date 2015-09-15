# django imports
from django.db import models

# external imports
from autoslug import AutoSlugField
from markupfield.fields import MarkupField


class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    @property
    def year_created(self):
        return str(self.created.year)

    @property
    def month_created(self):
        return self.created.strftime('%m')

    @property
    def day_created(self):
        return self.created.strftime('%d')


class Section(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    entry = models.ForeignKey('main.Entry')
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    body = MarkupField(markup_type='markdown', null=True, blank=True)

    def __unicode__(self):
        return self.title
