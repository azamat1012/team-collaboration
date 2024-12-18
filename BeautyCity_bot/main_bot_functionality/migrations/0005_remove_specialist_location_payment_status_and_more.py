# Generated by Django 5.1.4 on 2024-12-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_bot_functionality', '0004_payment_specialist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='location',
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='biography',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialization',
            field=models.CharField(choices=[('Стрижка волос', 'Стрижка волос'), ('Борода', 'Борода'), ('Укладка волос', 'Укладка волос'), ('Окрашиванаие волос', 'Окрашиванаие волос'), ('Уход за лицом', 'Уход за лицом')], max_length=200),
        ),
    ]
