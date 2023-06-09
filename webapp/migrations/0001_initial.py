# Generated by Django 4.1.6 on 2023-04-17 08:01

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50, verbose_name='Проект')),
                ('text', models.TextField(max_length=2000, verbose_name='Описание')),
                ('date_start', models.CharField(max_length=20, verbose_name='Начало')),
                ('date_end', models.CharField(max_length=20, verbose_name='Завершение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('users', models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('change_project_users', 'Can change the users of project')],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='Тип')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'Выполняется'), ('done', 'Завершена')], default='new', max_length=20, verbose_name='Статус')),
                ('title', models.CharField(max_length=100, verbose_name='Задача')),
                ('text', models.TextField(max_length=2000, verbose_name='Описание')),
                ('deadline', models.CharField(max_length=20, verbose_name='Исполнить до')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='todo', to='webapp.project', verbose_name='Project')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='todo', to='webapp.type', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
