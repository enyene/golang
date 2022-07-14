# Generated by Django 4.0.4 on 2022-07-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=2)),
                ('options', models.CharField(choices=[('g', 'grocery'), ('i', 'equipment'), ('s', 'sport')], max_length=5)),
            ],
        ),
    ]
