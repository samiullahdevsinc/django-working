# Generated by Django 4.1.4 on 2023-07-25 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='user1',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='user',
            new_name='user1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='user1',
        ),
    ]
