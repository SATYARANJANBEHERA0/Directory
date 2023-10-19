# Generated by Django 3.2.9 on 2023-10-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='teacher_profile_pics/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('room_number', models.CharField(max_length=10)),
                ('employee_number', models.CharField(max_length=10)),
                ('subjects_taught', models.CharField(max_length=200)),
            ],
        ),
    ]