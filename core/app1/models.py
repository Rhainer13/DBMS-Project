from django.db import models

# Create your models here.
class Resident(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField() 
    gender = models.CharField(max_length=1)
    purok = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'