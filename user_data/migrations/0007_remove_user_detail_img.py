# Generated by Django 4.2.7 on 2023-11-30 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0006_alter_user_detail_users_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_detail',
            name='img',
        ),
    ]
