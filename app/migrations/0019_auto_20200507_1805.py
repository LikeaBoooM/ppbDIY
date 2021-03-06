# Generated by Django 3.0.5 on 2020-05-07 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0018_auto_20200507_0939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentPost',
        ),
        migrations.CreateModel(
            name='CommentProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('ddate_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Project')),
            ],
        ),
    ]
