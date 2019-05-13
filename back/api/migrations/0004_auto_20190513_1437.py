# Generated by Django 2.2 on 2019-05-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190512_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='Abay str. 64', max_length=100),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='avg_cost',
            field=models.IntegerField(default=4500),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='contact',
            field=models.CharField(default='+7 (701) 979 80 73', max_length=100),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image_url',
            field=models.CharField(default='https://www.buro247.kz/images/Restaurants-Almaty-Spring-2016-13.jpg', max_length=255),
        ),
    ]