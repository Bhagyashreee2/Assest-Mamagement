# Generated by Django 5.0.4 on 2024-04-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modules", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="Password",
            new_name="Re_type_Your_password",
        ),
        migrations.RemoveField(
            model_name="user",
            name="Re_type_Your_Password",
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=50),
        ),
    ]
