# Generated by Django 3.2.7 on 2021-09-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priyanshu', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
