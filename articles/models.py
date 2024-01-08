from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from ckeditor.fields import RichTextField

class Article(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=200, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='authors')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={
            'pk': self.pk, 'slug': self.slug})

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    text = models.CharField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment(pk={self.pk}, author="{self.author}")'

    def get_absolute_url(self):
        return reverse('article_list')


    class Meta:
        ordering = ['-created']








