# Generated by Django 3.0.5 on 2020-05-20 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20200520_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='Opis',
        ),
    ]