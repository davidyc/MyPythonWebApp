# Generated by Django 2.2 on 2019-12-15 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evolution', '0002_auto_20191215_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='theme',
        ),
        migrations.CreateModel(
            name='PhaseTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution.Phase')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution.Theme')),
            ],
        ),
    ]
