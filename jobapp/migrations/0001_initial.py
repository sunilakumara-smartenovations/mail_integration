# Generated by Django 3.2.4 on 2022-08-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobdesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('roles_rensponsibilities', models.CharField(max_length=255, null=True)),
                ('recriter_details', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
