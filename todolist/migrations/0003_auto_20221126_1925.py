# Generated by Django 3.2.1 on 2022-11-26 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20221126_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='todolist',
            new_name='todo',
        ),
        migrations.AlterModelTable(
            name='todolist',
            table='Todolist',
        ),
    ]
