# Generated by Django 2.1.7 on 2019-03-23 07:40

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0016_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title'),
        ),
    ]