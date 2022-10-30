# Generated by Django 3.2 on 2022-10-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_birth_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('categoria', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
