# Generated by Django 4.2.10 on 2024-03-27 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_profile',
        ),
    ]