# Generated by Django 4.1 on 2023-03-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodid', models.IntegerField()),
                ('food_name', models.CharField(max_length=100)),
                ('food_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
