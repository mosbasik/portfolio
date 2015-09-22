# django imports
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import format_html

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

    @classmethod
    def get_ordered(cls, scope='displayed', count=None):
        if scope not in ['displayed', 'all']:
            return None

        if scope == 'displayed':
            return cls.objects.filter(display=True).order_by('-display_date')[:count]
        return cls.objects.all().order_by('-display_date')[:count]

    # @classmethod
    # def url(cls):
    #     base_url = None
    #     if cls == BlogEntry:
    #         base_url = 'blog_details'
    #     elif cls == ProjectEntry:
    #         base_url = 'project_details'
    #     url = reverse(base_url, args=(self.year, self.month, self.day, self.slug))
    #     return format_html('<a target="_blank" href="{url}">{url}</a>', url=url)


class BlogEntry(Entry):

    @property
    def url(self):
        url = reverse('blog_details', args=(self.year, self.month, self.day, self.slug))
        return format_html('<a target="_blank" href="{url}">{url}</a>', url=url)

    class Meta:
        verbose_name_plural = "Blog Entries"

    def __unicode__(self):
        return "Blog {}".format(self.title)


class ProjectEntry(Entry):

    @property
    def url(self):
        url = reverse('project_details', args=(self.year, self.month, self.day, self.slug))
        return format_html('<a target="_blank" href="{url}">{url}</a>', url=url)

    class Meta:
        verbose_name_plural = "Project Entries"

    def __unicode__(self):
        return "Project {}".format(self.title)
