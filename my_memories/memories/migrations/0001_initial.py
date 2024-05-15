# Generated by Django 5.0.6 on 2024-05-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('name', models.CharField(max_length=255)),
                ('memory', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
