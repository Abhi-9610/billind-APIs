# Generated by Django 5.0 on 2024-04-06 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_employee_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='username',
        ),
    ]
