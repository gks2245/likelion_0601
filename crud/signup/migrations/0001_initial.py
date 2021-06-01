# Generated by Django 3.2.3 on 2021-06-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
                ('email', models.EmailField(max_length=100)),
                ('introduce', models.TextField()),
            ],
        ),
    ]
