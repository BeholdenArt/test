# Generated by Django 3.2.7 on 2021-09-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priyanshu', '0004_auto_20210917_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=40),
        ),
    ]
