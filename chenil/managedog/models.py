from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    num_id = models.PositiveIntegerField()
    dog_master = models.ForeignKey(User, on_delete=models.CASCADE)