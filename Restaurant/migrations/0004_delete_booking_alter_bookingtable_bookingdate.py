# Generated by Django 4.2.7 on 2023-11-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0003_alter_bookingtable_bookingdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.AlterField(
            model_name='bookingtable',
            name='bookingDate',
            field=models.DateField(),
        ),
    ]
