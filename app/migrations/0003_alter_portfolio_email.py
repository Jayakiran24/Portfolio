# Generated by Django 5.1.2 on 2025-02-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_portfolio_message_alter_portfolio_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
