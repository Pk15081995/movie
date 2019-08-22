from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    budget=models.TextField()
    discription=models.TextField()
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def summary(self):
        return self.discription[0:25]
    def __str__(self):
        return self.title


# Create your models here.
