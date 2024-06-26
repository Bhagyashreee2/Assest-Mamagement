# Generated by Django 5.0.4 on 2024-04-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modules", "0002_rename_password_user_re_type_your_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="Email",
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="First_Name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="user",
            name="Last_Name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="user",
            name="Re_type_Your_password",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=250),
        ),
    ]
