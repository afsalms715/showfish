# Generated by Django 3.2.9 on 2021-12-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_bookshop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshop',
            name='img',
            field=models.ImageField(default='hhhh.png', upload_to='pics'),
        ),
    ]