from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Roaster(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class RoastLevel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Acidity(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CuppingNote(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Coffee(models.Model):
    name = models.CharField(max_length=250)
    roaster = models.ForeignKey("Roaster", on_delete=models.CASCADE) # CASCADE part makes sure the roaster info is deleted when a coffee is deleted
    origin = models.ManyToManyField("Country", related_name="coffees",blank=True) # Can search all coffees from a country using [country_name].coffees
    roast_level = models.ForeignKey("RoastLevel",on_delete=models.CASCADE,blank=True,null=True)
    acidity = models.ForeignKey("Acidity",on_delete=models.CASCADE,blank=True,null=True)
    cupping_notes = models.ManyToManyField("CuppingNote", related_name = "coffees",blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    comments = models.TextField(blank=True) 

    def __str__(self):
        return self.name


