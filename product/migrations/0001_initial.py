# Generated by Django 3.2.6 on 2021-08-19 06:50

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
                ('name', models.CharField(max_length=150, unique=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('measure', models.CharField(choices=[('p', 'шт.'), ('k', 'кг'), ('l', 'л')], max_length=1)),
                ('price', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
