# Generated by Django 5.1.4 on 2024-12-24 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_childvaccinehistory_date_given'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childvaccinehistory',
            old_name='visit',
            new_name='visit_number',
        ),
    ]