# Generated by Django 5.0.4 on 2024-08-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_baseuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
