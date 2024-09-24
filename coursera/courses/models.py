from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=6)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
  

    


# Create your models here.
