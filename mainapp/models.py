from django.db import models
from django.core.validators import FileExtensionValidator

class ImageModel(models.Model):
    img_comment = models.CharField(max_length=120)
    img_file = models.FileField(upload_to='images', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','gif'])])

    def __str__(self):
        return self.img_comment
