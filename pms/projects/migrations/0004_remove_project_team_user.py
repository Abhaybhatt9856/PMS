# Generated by Django 4.2.10 on 2024-03-19 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_team_user_project_team_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_team',
            name='user',
        ),
    ]