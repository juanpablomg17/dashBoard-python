# Generated by Django 3.2 on 2022-10-30 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20221030_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='death',
            old_name='name',
            new_name='year',
        ),
    ]