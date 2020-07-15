from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator


class EBook(models.Model):
    title = models.CharField(max_length=100, blank=False)
    file = models.FileField(upload_to='pdfs', validators=[
                            FileExtensionValidator(['pdf'])])
    thumbnail = models.ImageField(default='default/pdf_default.png')
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.SmallIntegerField()

    authors = models.ManyToManyField(
        'Author', related_name="ebook", blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def ebook_category(self):
        if self.category:
            return 'E-Book'
        else:
            return 'Note'

    ebook_category.short_description = 'catergory'


class Author(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title
