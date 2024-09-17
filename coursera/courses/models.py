from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=10)
    
    #contributors = models.ManyToMany()

    def __str__(self):
        return self.name
    

    


# Create your models here.
