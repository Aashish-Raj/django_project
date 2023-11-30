# Generated by Django 4.2.7 on 2023-11-30 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0002_user_detail_users_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ai_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('openai_model', models.CharField(max_length=50)),
                ('key', models.CharField(default='', max_length=255, null=True)),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_data.user_detail')),
            ],
        ),
    ]