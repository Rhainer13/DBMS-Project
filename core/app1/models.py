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

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    generic_name = models.CharField(blank=True)
    dosage = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.generic_name
    
class MedicineRequest(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.resident} requests {self.quantity} of {self.medicine}'

class ChildVaccineHistory(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    visit_number = models.PositiveIntegerField()
    vaccine_name = models.TextField(max_length=100)
    health_worker = models.CharField(max_length=50)
    date_given = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['resident']

    def __str__(self):
        return f'{self.resident} has been given {self.vaccine_name} on {self.date_given}'