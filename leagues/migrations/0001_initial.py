# Generated by Django 4.1.7 on 2023-04-28 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competition')),
            ],
            options={
                'verbose_name_plural': 'Leagues',
            },
        ),
    ]