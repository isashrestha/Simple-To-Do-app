# Generated by Django 3.2.1 on 2022-11-26 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todoNote',
            new_name='todolist',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='notes',
            new_name='todolist',
        ),
        migrations.AlterModelTable(
            name='todolist',
            table='todolist',
        ),
    ]