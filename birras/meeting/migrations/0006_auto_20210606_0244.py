# Generated by Django 3.1.7 on 2021-06-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0005_auto_20210606_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
