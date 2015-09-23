# django imports
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import format_html

# external imports
from autoslug import AutoSlugField
from markupfield.fields import MarkupField


class MarkupBlock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    body = MarkupField(markup_type='custom_markup', null=True, blank=True)

    def __unicode__(self):
        return str(self.body)


class TextBlock(MarkupBlock):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    @staticmethod
    def get(name, heading=None):
        block_heading = '' if heading is None else heading
        try:
            return TextBlock.objects.get(name=name)
        except TextBlock.DoesNotExist:
            textblock, created = TextBlock.objects.get_or_create(
                name='_default_%s' % name,
                body='%s\n\nSection is under development.' % block_heading
            )
            return textblock


class Entry(MarkupBlock):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    display_date = models.DateTimeField()
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
    def get_ordered(cls, display=None, count=None):
        if display is None:
            qs = cls.objects.all()
        elif display is True:
            qs = cls.objects.filter(diplay=True)
        elif display is False:
            qs = cls.objects.filter(display=False)
        else:
            return None
        return qs.order_by('-display_date')[:count]

    @property
    def next(self):
        next_entries = self.__class__.objects.filter(
            display=True,
            display_date__gt=self.display_date,
        ).order_by('display_date')
        try:
            print next_entries[0]
            return next_entries[0]
        except IndexError:
            return None

    @property
    def previous(self):
        previous_entries = self.__class__.objects.filter(
            display=True,
            display_date__lt=self.display_date,
        ).order_by('-display_date')
        try:
            print previous_entries[0]
            return previous_entries[0]
        except IndexError:
            return None


class Blog(Entry):

    @property
    def url(self):
        url = reverse('blog_details', args=(self.year, self.month, self.day, self.slug))
        return format_html('<a target="_blank" href="{url}">{url}</a>', url=url)


class Project(Entry):

    @property
    def url(self):
        url = reverse('project_details', args=(self.year, self.month, self.day, self.slug))
        return format_html('<a target="_blank" href="{url}">{url}</a>', url=url)


class LocalFile(models.Model):
    contents = models.FileField()

    def __unicode__(self):
        return self.contents.name
