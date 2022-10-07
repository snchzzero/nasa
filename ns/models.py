from django.db import models
from filer.fields.image import FilerImageField


class My_image(models.Model):
    title = models.CharField(max_length=255)
    cover = FilerImageField(related_name="image_covers", on_delete=models.CASCADE)


