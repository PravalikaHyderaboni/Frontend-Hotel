# Generated by Django 4.1 on 2023-03-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_remove_food_foodid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]