# Generated by Django 3.2.7 on 2021-09-18 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('priyanshu', '0009_resume_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume',
            new_name='link',
        ),
    ]
