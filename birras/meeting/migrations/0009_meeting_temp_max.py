# Generated by Django 3.1.7 on 2021-06-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0008_auto_20210607_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='temp_max',
            field=models.CharField(max_length=50, null=True),
        ),
    ]