# Generated by Django 3.0.5 on 2020-05-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
