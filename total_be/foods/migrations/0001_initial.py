# Generated by Django 5.0.4 on 2024-06-20 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unit', models.CharField(choices=[('0', 'custom'), ('1', 'g'), ('2', 'oz'), ('3', 'lb(s)'), ('4', 'cup(s)'), ('5', 'tbsp'), ('6', 'tsp'), ('7', 'serving(s)')], max_length=1)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbs', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=6)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUnitOfMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.measure')),
            ],
        ),
    ]
