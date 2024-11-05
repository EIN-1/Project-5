# Generated by Django 4.2.16 on 2024-10-31 12:04

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=254)),
                ('instructor', models.CharField(max_length=254)),
                ('courseUrl', models.URLField(blank=True, max_length=1024, null=True)),
                ('imageUrl', models.URLField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('reviews', models.IntegerField(blank=True, null=True)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lectures', models.IntegerField(blank=True, null=True)),
                ('level', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flag', models.BooleanField(default=False)),
                ('students', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
