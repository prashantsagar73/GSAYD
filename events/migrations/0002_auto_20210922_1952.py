# Generated by Django 3.2.7 on 2021-09-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
