from django.db import models
from django.core.exceptions import ValidationError


class Theme(models.Model):
    name = models.CharField(max_length=32)
    template = models.TextField()

    def __unicode__(self):
        return self.name

class Directory(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('Directory',
        null=True,
        blank=True,
        related_name='subdirectories',
    )
    theme = models.ForeignKey(Theme, default=1)

    def depth(self):
        directory = self
        count = 0
        while directory.parent is not None:
            count += 1
            directory = directory.parent
        return count

    @property
    def index_page(self):
        return Page.objects.get(name="", directory=self)

    @property
    def non_index_pages(self):
        return Page.objects.exclude(name="").filter(directory=self).order_by('name')

    def __unicode__(self):
        if self.pk == 0:
            return ''
        return self.parent.__unicode__() + '/' + self.name

    class Meta:
        verbose_name_plural = 'Directories'


class Page(models.Model):
    name = models.CharField(max_length=32, blank=True)
    directory = models.ForeignKey('Directory', related_name='pages')
    title = models.CharField(max_length=100)
    contents = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/page/%Y/')
    footer_link = models.BooleanField(default=False,
        help_text='Should this page appear in the footer?')

    class Meta:
        unique_together = (
            ('name', 'directory'),
        )


    def __unicode__(self):
        return unicode(self.directory) + '/' + self.name

    def get_absolute_url(self):
        return '/' + self.path

    @classmethod
    def from_path(cls, path):
        try:
            parts = path.split('/')
            directories = parts[:-1]
            page = parts[-1]
            directory = Directory.objects.get(parent=None)
            for subdir in directories:
                directory = Directory.objects.get(parent=directory, name=subdir)
            try:
                return cls.objects.get(directory=directory, name=page)
            except cls.DoesNotExist:
                return cls(name=page, directory=directory)
        except Exception:
            raise cls.DoesNotExist()

    @property
    def path(self):
        parts = []
        d = self.directory
        while d.parent is not None:
            parts.insert(0, d.name)
            d = d.parent
        return '/'.join(parts + [self.name])

