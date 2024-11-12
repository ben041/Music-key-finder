from django.db import models
from django.core.files.storage import FileSystemStorage
import os

class AudioFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Analysis results
    key = models.CharField(max_length=20, blank=True)
    alternative_key = models.CharField(max_length=20, blank=True, null=True)
    correlation = models.FloatField(null=True)
    alternative_correlation = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.file.name} - {self.key}"
    
    def delete(self, *args, **kwargs):
        # Delete the file when the model instance is deleted
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)