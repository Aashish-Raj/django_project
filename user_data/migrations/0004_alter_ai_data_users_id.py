# Generated by Django 4.2.7 on 2023-11-30 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_data', '0003_ai_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_data',
            name='users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
