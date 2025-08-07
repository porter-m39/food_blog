from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# using this temporarily while I import old date
from django.utils import timezone

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
    
class Critic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Score(models.Model):
    critic = models.ForeignKey("Critic",  on_delete=models.CASCADE) # CASCADE part makes sure the roaster info is deleted when a coffee is deleted
    coffee = models.ForeignKey("Coffee", on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    #created_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(default=timezone.now, null=True, blank=True)

    # the following function is courtesy of Deep Seek. No migration needed when defining this.
    def __str__(self):
        # Get the critic's name (assuming Critic model has a name field)
        critic_name = str(self.critic)
        
        # Get coffee name if it exists (handling the null case)
        coffee_name = str(self.coffee)
        
        return f"{critic_name} - {coffee_name}: {self.score}/10"


class Coffee(models.Model):
    name = models.CharField(max_length=250)
    roaster = models.ForeignKey("Roaster", on_delete=models.CASCADE) # CASCADE part makes sure the roaster info is deleted when a coffee is deleted
    origin = models.ManyToManyField("Country", related_name="coffees",blank=True) # Can search all coffees from a country using [country_name].coffees
    roast_level = models.ForeignKey("RoastLevel",on_delete=models.CASCADE,blank=True,null=True)
    acidity = models.ForeignKey("Acidity",on_delete=models.CASCADE,blank=True,null=True)
    cupping_notes = models.ManyToManyField("CuppingNote", related_name = "coffees",blank=True)
    #created_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(default=timezone.now, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    comments = models.TextField(blank=True) 

    def __str__(self):
        return self.name


