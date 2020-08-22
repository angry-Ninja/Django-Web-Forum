# Generated by Django 3.0.8 on 2020-07-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_replies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='topic',
            name='views',
            field=models.FloatField(default=0),
        ),
    ]
