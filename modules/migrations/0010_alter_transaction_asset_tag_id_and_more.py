# Generated by Django 5.0.4 on 2024-04-22 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modules", "0009_rename_asset_transaction_asset_tag_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="Asset_Tag_ID",
            field=models.ForeignKey(
                db_column="Asset_Tag_ID",
                on_delete=django.db.models.deletion.CASCADE,
                to="modules.asset",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="Assigned_To",
            field=models.ForeignKey(
                blank=True,
                db_column="Assigned_To",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="modules.employee",
            ),
        ),
    ]
