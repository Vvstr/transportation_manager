# Generated by Django 5.1.4 on 2024-12-25 14:36

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Crop",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("group", models.CharField(blank=True, max_length=20, null=True)),
                ("first_name", models.CharField(blank=True, max_length=30, null=True)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "username",
                    models.CharField(blank=True, max_length=30, null=True, unique=True),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="FertilizationSchedule",
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
                ("planned_date", models.DateField()),
                ("actual_date", models.DateField(blank=True, null=True)),
                ("resources_used", models.TextField(blank=True, null=True)),
                (
                    "crop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fertilization_schedules",
                        to="greenhouses.crop",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Greenhouse",
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
                ("name", models.CharField(max_length=100)),
                ("crop_type", models.CharField(max_length=100)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="greenhouses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="crop",
            name="green_house",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="crops",
                to="greenhouses.greenhouse",
            ),
        ),
        migrations.CreateModel(
            name="HarvestSchedule",
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
                ("planned_date", models.DateField()),
                ("actual_date", models.DateField(blank=True, null=True)),
                ("resources_used", models.TextField(blank=True, null=True)),
                (
                    "crop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="harvest_schedules",
                        to="greenhouses.crop",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IrrigationSchedule",
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
                ("planned_date", models.DateField()),
                ("actual_date", models.DateField(blank=True, null=True)),
                ("resources_used", models.TextField(blank=True, null=True)),
                (
                    "crop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="irrigation_schedules",
                        to="greenhouses.crop",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SowingSchedule",
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
                ("planned_date", models.DateField()),
                ("actual_date", models.DateField(blank=True, null=True)),
                ("resources_used", models.TextField(blank=True, null=True)),
                (
                    "crop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sowing_schedules",
                        to="greenhouses.crop",
                    ),
                ),
            ],
        ),
    ]
