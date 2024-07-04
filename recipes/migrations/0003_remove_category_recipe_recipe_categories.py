# Generated by Django 5.0.4 on 2024-06-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_category_recipe_category_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='recipes.category'),
        ),
    ]