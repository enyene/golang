# Generated by Django 4.0.4 on 2022-07-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(default='null@gmail.com', max_length=254)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['-city']},
        ),
    ]