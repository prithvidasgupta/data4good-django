# Generated by Django 2.1.1 on 2020-04-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
