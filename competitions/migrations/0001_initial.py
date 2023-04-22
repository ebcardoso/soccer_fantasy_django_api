import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Competition',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=255)),
        ('type', models.IntegerField()),
        ('final_date', models.DateField()),
        ('created_at', models.DateTimeField(default=datetime.datetime(2023, 4, 22, 18, 36, 57, 825767))),
        ('updated_at', models.DateTimeField(default=datetime.datetime(2023, 4, 22, 18, 36, 57, 825782))),
      ],
      options={
          'verbose_name_plural': 'Competitions',
      },
    ),
  ]
