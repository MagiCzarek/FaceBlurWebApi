import numpy as np
from django.db import models
from PIL import Image
from .util import get_blurred_face_image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.


class UploadedFile(models.Model):

    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # open image and convert to arr for opencv
        pil_img = Image.open(self.image)

        img_to_blur = np.array(pil_img)

        blurred_image = get_blurred_face_image(img_to_blur)

        piled_image = Image.fromarray(blurred_image)

        buffer = BytesIO()
        piled_image.save(buffer, format='png')

        result_image = buffer.getvalue()

        self.image.save(str(self.image),ContentFile(result_image),save=False)

        super().save(*args,**kwargs)
        
