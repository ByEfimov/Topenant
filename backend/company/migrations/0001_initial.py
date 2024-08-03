# Generated by Django 5.0.4 on 2024-08-03 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('applicant', models.BooleanField()),
                ('pointsHave', models.IntegerField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=600, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('pointsHave', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='company.company', verbose_name='Компания')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('rejected', 'Отклонено'), ('waiting', 'Ожидание'), ('approved', 'Принят')], default='waiting', max_length=15, verbose_name='Статус')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='Работник')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='company.works', verbose_name='Вакансия')),
            ],
        ),
    ]
