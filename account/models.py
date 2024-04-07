from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users',
                                blank=True, null=True)
    detail_photo = models.ImageField(upload_to='users', 
                                        null=True, blank=True)
    back_photo = models.ImageField(upload_to='users',
                                        null=True, blank=True)
    bio = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {{ self.user.username }}"
    
