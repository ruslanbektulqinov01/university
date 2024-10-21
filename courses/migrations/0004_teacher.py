# Generated by Django 5.0.6 on 2024-06-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_speciality_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
    ]
