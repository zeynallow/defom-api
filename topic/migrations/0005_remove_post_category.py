# Generated by Django 2.1.7 on 2019-03-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_auto_20190322_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
