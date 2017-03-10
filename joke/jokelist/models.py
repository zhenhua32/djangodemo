from django.db import models

# from django.utils import timezone


class CommonInfo(models.Model):
    title = models.CharField(max_length=100)
    pubdate = models.DateTimeField(auto_now_add=True)
    source = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class TextJoke(CommonInfo):
    content = models.TextField()


class ImgJoke(CommonInfo):
    content = models.ImageField(upload_to='img/%Y/%m/%d')


class VedioJoke(CommonInfo):
    content = models.FileField(upload_to='vedio/%Y/%m/%d')
