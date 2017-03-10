from django.contrib import admin
from .models import TextJoke, ImgJoke, VedioJoke

# Register your models here.
admin.site.register(TextJoke)
admin.site.register(ImgJoke)
admin.site.register(VedioJoke)
