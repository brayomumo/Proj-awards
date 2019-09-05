from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='posts/', default='')
    description = models.CharField(max_length=150)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title