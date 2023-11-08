# Generated by Django 4.2.7 on 2023-11-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('bithday', models.DateField()),
                ('document', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('salary', models.FloatField()),
                ('group', models.CharField(max_length=10)),
                ('function', models.CharField(max_length=50)),
                ('initial_at', models.DateField()),
                ('working', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('Famale', 'Famale'), ('Male', 'Male'), ('Others', 'Others')], max_length=10)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('observations', models.TextField()),
            ],
        ),
    ]
