# Generated by Django 2.2.10 on 2020-02-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifthapp', '0002_auto_20200204_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]