# Generated by Django 3.0.5 on 2020-05-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
    ]
