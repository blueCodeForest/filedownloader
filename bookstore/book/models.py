from django.db import models

class FileUpload(models.Model):
    files = models.FileField()

