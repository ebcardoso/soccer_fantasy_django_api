from django.db import migrations, models

class Migration(migrations.Migration):
  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Team',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=50)),
        ('name_complete', models.CharField(max_length=100)),
        ('city', models.CharField(max_length=50)),
        ('stadium', models.CharField(max_length=100)),
        ('founded_in', models.IntegerField()),
        ('status', models.IntegerField(default=1)),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True)),
      ],
      options={
        'verbose_name_plural': 'Teams',
      },
    ),
  ]
