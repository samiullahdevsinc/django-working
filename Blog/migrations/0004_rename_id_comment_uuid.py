# Generated by Django 4.1.4 on 2023-07-25 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_comment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='id',
            new_name='uuid',
        ),
    ]
