# Generated by Django 4.0.6 on 2022-10-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jm_realestate_app', '0002_alter_profit_earning'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproperty',
            name='p_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
