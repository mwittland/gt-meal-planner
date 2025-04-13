# Generated by Django 5.2 on 2025-04-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_mealplan_profile_mealplan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='current_dollars',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='current_swipes',
            field=models.IntegerField(default=0),
        ),
    ]
