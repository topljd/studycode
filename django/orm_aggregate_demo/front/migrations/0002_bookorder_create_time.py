# Generated by Django 3.0.5 on 2020-04-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
