# Generated by Django 2.2 on 2019-05-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuisine',
            new_name='Section',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='cuisine',
            new_name='section',
        ),
    ]
