# Generated by Django 2.1.1 on 2018-09-07 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cache_test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
