# Generated by Django 4.1.2 on 2022-11-06 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api_edition", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="advocate",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="company",
            options={"ordering": ["id"]},
        ),
        migrations.RemoveField(
            model_name="company",
            name="advocates",
        ),
    ]