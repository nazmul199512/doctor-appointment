# Generated by Django 2.2 on 2020-10-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_ambulance'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
