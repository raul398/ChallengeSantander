# Generated by Django 3.1.7 on 2021-06-05 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210604_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='staff',
            new_name='is_staff',
        ),
    ]
