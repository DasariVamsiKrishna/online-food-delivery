# Generated by Django 3.0 on 2022-05-07 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0007_auto_20220507_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.DeleteModel(
            name='Rolereq',
        ),
    ]