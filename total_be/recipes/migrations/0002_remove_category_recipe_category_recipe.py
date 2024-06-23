# Generated by Django 5.0.4 on 2024-06-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='recipe',
        ),
        migrations.AddField(
            model_name='category',
            name='recipe',
            field=models.ManyToManyField(to='recipes.recipe'),
        ),
    ]