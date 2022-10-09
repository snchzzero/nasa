from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class My_image(models.Model):
    title = models.CharField(max_length=255)
    cover = FilerImageField(related_name="image_covers", null=True, blank=True, on_delete=models.CASCADE)  #on_delete=models.CASCADE
    disclaimer = FilerFileField(null=True, blank=True,
                                related_name="image_covers_disclaimer", on_delete=models.CASCADE)
    def __str__(self):
        return self.title



