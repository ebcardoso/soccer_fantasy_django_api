# Generated by Django 4.1.7 on 2023-05-14 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rounds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='round',
            old_name='competition',
            new_name='competition_id',
        ),
    ]
