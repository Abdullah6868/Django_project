# Generated by Django 5.1.3 on 2024-11-20 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0004_alter_student_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="EducationHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("institution_name", models.CharField(max_length=200)),
                ("degree", models.CharField(max_length=100)),
                ("field_of_study", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(null=True)),
                ("grade", models.CharField(max_length=10, null=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eduction_history",
                        to="student.student",
                    ),
                ),
            ],
        ),
    ]
