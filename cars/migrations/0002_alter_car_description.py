# Generated by Django 4.1.7 on 2023-03-18 00:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
