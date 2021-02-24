from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def  __str__(self):
        return f"{self.name}"



class Food(models.Model):
    category= models.ForeignKey("Category",  on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    def __str__(self):
        return f"{self.name}"
        
        