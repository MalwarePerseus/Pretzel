from django.db import models

# Create your models here.
class Pretzels(models.Model)
     # theres alwaus an ID tag, on first pos, with primay key set to true
    content = models.TextField(blank=True, null=True)
    images = models.FileField(upload_to='images/', blank=True, null= True)


