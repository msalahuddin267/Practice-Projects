# Generated by Django 5.1.4 on 2024-12-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_schedular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CronJobControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('interval', models.PositiveIntegerField(default=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
