# Generated by Django 4.2.2 on 2023-06-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('jd', models.CharField(max_length=1000)),
                ('working_hour', models.CharField(max_length=100)),
                ('working_location', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_mobile', models.CharField(max_length=100)),
                ('contact_wechat', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('start_time', models.CharField(max_length=100)),
                ('advice', models.CharField(max_length=1000)),
            ],
        ),
    ]
