# django imports
from django.db import models

# external imports
from autoslug import AutoSlugField
from markupfield.fields import MarkupField


class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    display_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    body = MarkupField(markup_type='custom_markup', null=True, blank=True)
    display = models.BooleanField(default=False)

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


class BlogEntry(Entry):

    class Meta:
        verbose_name_plural = "Blog Entries"

    def __unicode__(self):
        return "Blog {}".format(self.title)


class ProjectEntry(Entry):

    class Meta:
        verbose_name_plural = "Project Entries"

    def __unicode__(self):
        return "Project {}".format(self.title)
