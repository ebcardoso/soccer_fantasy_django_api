from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
  initial = True

  dependencies = [
    ('competitions', '0001_initial'),
  ]

  operations = [
    migrations.CreateModel(
      name='Round',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=50)),
        ('final_date', models.DateField()),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True)),
        ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competition')),
      ],
      options={
        'verbose_name_plural': 'Rounds',
      },
    ),
  ]
