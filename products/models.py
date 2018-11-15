from django.db import models

# Create your models here.

class whiskey(models.Model):
    image=models.ImageField(upload_to='images/')
    item=models.CharField(max_length=50)

    def __str__(self):
        return self.item


class beer(models.Model):
    image = models.ImageField(upload_to='images/')
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item


class wine(models.Model):
    image = models.ImageField(upload_to='images/')
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item


class rum(models.Model):
    image = models.ImageField(upload_to='images/')
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item


class vodka(models.Model):
    image = models.ImageField(upload_to='images/')
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item
