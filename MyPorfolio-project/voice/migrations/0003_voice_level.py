# Generated by Django 3.1 on 2020-10-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0002_voice'),
    ]

    operations = [
        migrations.AddField(
            model_name='voice',
            name='level',
            field=models.CharField(default='Не указан', max_length=25),
        ),
    ]
