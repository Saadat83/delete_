# Generated by Django 4.1 on 2022-08-18 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='poat_date',
            new_name='post_date',
        ),
    ]
