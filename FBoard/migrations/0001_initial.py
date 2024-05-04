# Generated by Django 4.1.4 on 2024-02-17 11:46

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('healers', 'Хилы'), ('tanks', 'Танки'), ('dd', 'ДД'), ('dealers', 'Торговцы'), ('gildmasters', 'Гилдмастеры'), ('questgivers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potionsmakers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], max_length=25, verbose_name='Категория')),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=15, verbose_name='Названиe')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FBoard.post')),
            ],
        ),
    ]
