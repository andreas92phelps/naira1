# Generated by Django 4.2.5 on 2023-10-05 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_aboutme_remove_user_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]
