# Generated by Django 4.2.5 on 2023-10-05 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aboutme',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salary',
        ),
    ]
