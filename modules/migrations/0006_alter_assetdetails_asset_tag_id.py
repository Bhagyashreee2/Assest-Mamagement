# Generated by Django 5.0.4 on 2024-04-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modules", "0005_assetdetails_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetdetails",
            name="Asset_Tag_Id",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
