# Generated by Django 3.2.6 on 2021-08-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date',
            new_name='date_mod',
        ),
    ]