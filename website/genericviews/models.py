from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100,blank=True)
    location = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    mobile = models.CharField(max_length=15,blank=True)

    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name
