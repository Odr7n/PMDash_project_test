# Generated by Django 4.2.7 on 2023-12-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_account_options_alter_account_account_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="account_image",
        ),
    ]
