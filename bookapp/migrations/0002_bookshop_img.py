# Generated by Django 3.2.9 on 2021-12-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]