# Generated by Django 3.1.3 on 2024-03-19 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20240319_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
    ]
