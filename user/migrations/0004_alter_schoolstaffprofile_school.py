# Generated by Django 5.0.2 on 2024-02-23 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
        ('user', '0003_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolstaffprofile',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_staff', to='schools.school'),
        ),
    ]
