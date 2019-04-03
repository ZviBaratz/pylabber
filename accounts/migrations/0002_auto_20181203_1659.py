# Generated by Django 2.1.3 on 2018-12-03 16:59

import accounts.choices
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="title",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NONE", ""),
                    ("MSC", "MSc"),
                    ("PHD", "PhD"),
                    ("PROF", "Professor"),
                ],
                default=accounts.choices.Title(""),
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]