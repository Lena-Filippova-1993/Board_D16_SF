# Generated by Django 4.2.11 on 2024-04-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_authuser_code_remove_authuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
    ]
