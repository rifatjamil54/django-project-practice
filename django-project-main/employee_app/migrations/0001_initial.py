# Generated by Django 4.0.1 on 2022-02-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]