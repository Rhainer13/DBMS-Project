from django.db import models

# Create your models here.
class Resident(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField() 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    purok = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
    
# class Medicine(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self):
#         return self.name