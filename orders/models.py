from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=1)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} pizza of size {self.size} costs {self.price}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=1)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} sub of size {self.size} costs {self.price}"

class Platter(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=1)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} platter of size {self.size} costs {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} costs {self.price}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} pasta costs {self.price}"

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"