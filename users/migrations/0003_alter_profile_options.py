# Generated by Django 4.1.2 on 2022-10-13 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]