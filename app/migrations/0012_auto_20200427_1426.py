# Generated by Django 3.0.5 on 2020-04-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_project_miniature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='miniature',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
