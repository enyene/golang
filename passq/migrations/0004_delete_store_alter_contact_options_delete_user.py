# Generated by Django 4.0.4 on 2022-07-13 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passq', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'default_permissions': (), 'permissions': (('can comment', 'user can comment'), ('can edit', 'usr can edit comment'))},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
