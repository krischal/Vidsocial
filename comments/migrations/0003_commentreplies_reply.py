# Generated by Django 2.1.4 on 2019-01-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190106_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreplies',
            name='reply',
            field=models.TextField(default=''),
        ),
    ]
