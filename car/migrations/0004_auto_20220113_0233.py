# Generated by Django 3.2.3 on 2022-01-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20220113_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='white', max_length=100),
        ),
    ]
