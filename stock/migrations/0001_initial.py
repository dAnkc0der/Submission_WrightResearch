# Generated by Django 4.1.5 on 2023-11-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
