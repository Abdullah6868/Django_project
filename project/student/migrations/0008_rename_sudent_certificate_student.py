# Generated by Django 5.1.3 on 2024-11-21 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0007_alter_certificate_certificate_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificate",
            old_name="sudent",
            new_name="student",
        ),
    ]
