# Generated by Django 3.2.25 on 2024-07-28 17:19

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240721_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]