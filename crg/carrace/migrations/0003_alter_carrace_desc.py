# Generated by Django 3.2.2 on 2021-05-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrace', '0002_alter_carrace_time_limti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrace',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]