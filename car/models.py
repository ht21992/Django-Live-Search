from django.db import models

# Create your models here.


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    make = models.CharField(max_length=200, null=False)
    model = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=100, default='white',null=False)
    img = models.ImageField(upload_to="car_images/")

    def __str__(self):
        return f"{self.make} - {self.model}"

