from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    tip = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
