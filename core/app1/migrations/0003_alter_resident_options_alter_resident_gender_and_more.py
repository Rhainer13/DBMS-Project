# Generated by Django 5.1.4 on 2024-12-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_resident_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resident',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='resident',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='resident',
            name='purok',
            field=models.CharField(choices=[('Saging', 'Saging'), ('Manga', 'Manga'), ('Cassava', 'Cassava'), ('Camote', 'Camote'), ('Bayabas', 'Bayabas'), ('Ampalaya', 'Ampalaya'), ('Kapayas', 'Kapayas'), ('Talong', 'Talong'), ('Sili', 'Sili'), ('Batong', 'Batong'), ('Agbate', 'Agbate'), ('Gabi', 'Gabi')], max_length=20),
        ),
    ]