# django imports
from django.db import models

# external imports
from autoslug import AutoSlugField
from markupfield.fields import MarkupField


class Entry(models.Model):

    KIND_CHOICES = (
        ('Blog', 'Blog'),
        ('Blog', 'Project'),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    display_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    kind = models.CharField(choices=KIND_CHOICES, max_length=50)

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

    @property
    def ordered_sections(self):
        return self.section_set.order_by('order', 'created')


class Section(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    entry = models.ForeignKey('main.Entry')
    order = models.IntegerField()
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    body = MarkupField(markup_type='markdown', null=True, blank=True)

    def __unicode__(self):
        return "{} - {}".format(self.entry.title, self.title)
