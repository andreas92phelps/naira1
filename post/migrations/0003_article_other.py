# Generated by Django 4.2.5 on 2023-10-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_article_title_alter_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='other',
            field=models.ImageField(default='', upload_to='post'),
        ),
    ]
