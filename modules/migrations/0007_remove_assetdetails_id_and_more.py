# Generated by Django 5.0.4 on 2024-04-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modules", "0006_alter_assetdetails_asset_tag_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assetdetails",
            name="id",
        ),
        migrations.AlterField(
            model_name="assetdetails",
            name="Asset_Tag_Id",
            field=models.CharField(
                max_length=30, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
