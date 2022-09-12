from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Files(models.Model):
    title = models.CharField(max_length=200)
    uploadfile = models.FileField(upload_to='upload_files/%Y/%m/%d/', verbose_name='Files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date_file')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Files"
        verbose_name_plural = "Files"
        ordering = ['-created_at']
