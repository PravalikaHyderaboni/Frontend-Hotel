from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Food(models.Model):
    def __str__(self):
        return self.food_name
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=100)
    food_img = models.CharField(max_length=500)


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
