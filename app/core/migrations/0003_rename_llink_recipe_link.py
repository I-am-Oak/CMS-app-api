# Generated by Django 3.2.4 on 2024-02-13 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20240213_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='llink',
            new_name='link',
        ),
    ]
