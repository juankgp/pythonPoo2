# Generated by Django 3.0.5 on 2020-08-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fempleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDep', models.CharField(max_length=25)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
