# Generated by Django 5.1.2 on 2025-03-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=220)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
