# Generated by Django 3.2.3 on 2022-01-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
