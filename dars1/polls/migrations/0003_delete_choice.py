# Generated by Django 4.1.7 on 2023-03-31 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
