# Generated by Django 4.1 on 2023-03-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_img',
            field=models.CharField(max_length=500),
        ),
    ]
