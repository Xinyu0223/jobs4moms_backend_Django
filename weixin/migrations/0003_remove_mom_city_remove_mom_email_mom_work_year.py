# Generated by Django 4.2.2 on 2023-09-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0002_employer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mom',
            name='city',
        ),
        migrations.RemoveField(
            model_name='mom',
            name='email',
        ),
        migrations.AddField(
            model_name='mom',
            name='work_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
