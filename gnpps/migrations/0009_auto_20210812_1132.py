# Generated by Django 3.2.4 on 2021-08-12 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0008_auto_20210811_0933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='picture1',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='services',
            name='picture2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='picture3',
        ),
    ]
