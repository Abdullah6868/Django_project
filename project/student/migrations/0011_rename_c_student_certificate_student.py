# Generated by Django 5.1.3 on 2024-11-24 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0010_rename_student_certificate_c_student"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificate",
            old_name="c_student",
            new_name="student",
        ),
    ]