# Generated by Django 2.0.2 on 2018-02-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodel',
            name='seller_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='seller_phone_no',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]