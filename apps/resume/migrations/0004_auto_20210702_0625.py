# Generated by Django 3.1.12 on 2021-07-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210702_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='user',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hobbies',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='user',
        ),
        migrations.AlterField(
            model_name='experience',
            name='role',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skills',
            field=models.CharField(max_length=100),
        ),
    ]
