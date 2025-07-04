from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_upload_images')
    contact_number = models.CharField(max_length=50, default="+789456213")

    def __str__(self):
        return self.user.username