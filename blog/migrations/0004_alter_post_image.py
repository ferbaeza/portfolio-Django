# Generated by Django 4.1 on 2022-08-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_image2_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
