# Generated by Django 4.1.7 on 2023-02-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feeds", "0003_alter_feed_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="contentImg",
            field=models.URLField(max_length=1000),
        ),
    ]
