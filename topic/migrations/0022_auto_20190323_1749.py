# Generated by Django 2.1.7 on 2019-03-23 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0021_auto_20190323_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='topic.Post'),
        ),
    ]