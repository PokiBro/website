# Generated by Django 3.2.13 on 2022-06-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220603_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]