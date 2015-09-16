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
    body = MarkupField(markup_type='markdown', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    @property
    def year(self):
        return str(self.display_date.year)

    @property
    def month(self):
        return self.display_date.strftime('%m')

    @property
    def day(self):
        return self.display_date.strftime('%d')

    @property
    def ordered_sections(self):
        return self.section_set.order_by('order', 'created')
