# Generated by Django 4.1.2 on 2022-11-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_edition", "0006_alter_advocate_url_alter_company_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advocate",
            name="short_bio",
            field=models.CharField(max_length=150),
        ),
    ]
