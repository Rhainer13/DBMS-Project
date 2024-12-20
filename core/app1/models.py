from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Resident(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    PUROK_CHOICES = [
        ('Saging', 'Saging'),
        ('Manga', 'Manga'),
        ('Cassava', 'Cassava'),
        ('Camote', 'Camote'),
        ('Bayabas', 'Bayabas'),
        ('Ampalaya', 'Ampalaya'),
        ('Kapayas', 'Kapayas'),
        ('Talong', 'Talong'),
        ('Sili', 'Sili'),
        ('Batong', 'Batong'),
        ('Agbate', 'Agbate'),
        ('Gabi', 'Gabi'),
    ]
    
    phone_number_validator = RegexValidator(
        regex=r'^\d{11}$',
        message='Phone number must be exactly 11 digits.'
    )

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField() 
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)
    purok = models.CharField(max_length=20, choices=PUROK_CHOICES, blank=False)
    phone_number = models.CharField(max_length=11, validators=[phone_number_validator])
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

# class Medicine(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self):
#         return self.name