# Generated by Django 5.0.1 on 2024-03-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("messenger", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="thread",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]