# Generated by Django 3.2 on 2022-10-30 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_death_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='death',
            old_name='quantity',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='death',
            old_name='category',
            new_name='categoria',
        ),
    ]