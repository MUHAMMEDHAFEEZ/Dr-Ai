from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    #Check the conditions that apply to you or to any members of your immediate relatives
    #immediate_relatives= models.CharField(max_length=50, blank=True, null=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username