from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f"{self.title}"

class Applications(models.Model):
    title = models.CharField(max_length=100)
    link_comment = RichTextUploadingField()
    order = models.IntegerField(null=True)

    class Meta:
        verbose_name = ("applications")

    def __str__(self):
        return f"{self.title}"

class MostUsedApp(models.Model):
    title = models.CharField(max_length=100)
    link = RichTextUploadingField()

    class Meta:
        verbose_name = ("mostusedapp")

    def __str__(self):
        return f"{self.title}"


class About(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    class Meta:
        verbose_name = ("about")

    def __str__(self):
        return f"{self.title}"


class ApplicationsPost(models.Model):

    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    class Meta:
        verbose_name = ("applicationspost")

    def __str__(self):
        return f"{self.title}"


class Sherbime(models.Model):
    title = models.CharField(max_length=100)
    link = RichTextUploadingField()

    class Meta:
        verbose_name = ("sherbime")

    def __str__(self):
        return f"{self.title}"

class Formular(models.Model):
    title = models.CharField(max_length=100)
    link = RichTextUploadingField()

    class Meta:
        verbose_name = ("formular")

    def __str__(self):
        return f"{self.title}"

class BazaLigjore(models.Model):
    title = models.CharField(max_length=100)
    link = RichTextUploadingField()

    class Meta:
        verbose_name = ("bazaligjore")

    def __str__(self):
        return f"{self.title}"

class TestZone(models.Model):
    title = models.CharField(max_length=100)
    link = RichTextUploadingField()

    class Meta:
        verbose_name = ("testzone")

    def __str__(self):
        return f"{self.title}"

class Manuale(models.Model):
    title = models.CharField(max_length=100)
    link = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("manuale")



