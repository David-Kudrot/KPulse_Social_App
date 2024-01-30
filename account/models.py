from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='account/images/', default="https://t4.ftcdn.net/jpg/05/89/93/27/360_F_589932782_vQAEAZhHnq1QCGu5ikwrYaQD0Mmurm0N.jpg", null=True, blank=True)
    cover_image = models.ImageField(upload_to="account/images/", null=True, blank=True, default="https://www.nicepng.com/png/full/959-9595523_blank-facebook-cover-ivory.png")
    phone_number = models.CharField(max_length=15)
    bio = models.TextField()
    friends = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name}"