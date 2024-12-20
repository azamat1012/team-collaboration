# Generated by Django 5.1.4 on 2024-12-19 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_bot_functionality', '0007_salon'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_week', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], max_length=11)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_hours', to='main_bot_functionality.salon')),
            ],
        ),
    ]
