# Generated by Django 5.0.2 on 2024-02-26 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
        ('user', '0005_user_is_email_confirmed_emailconfirmationtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolstaffprofile',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_staffs', to='schools.school'),
        ),
    ]
