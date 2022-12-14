# Generated by Django 3.0 on 2022-05-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0006_auto_20210708_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('items', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Guest'), (2, 'Manager'), (3, 'User')], default=3),
        ),
    ]
