# Generated by Django 2.2 on 2021-05-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=99)),
                ('description', models.TextField(default=None)),
            ],
        ),
    ]