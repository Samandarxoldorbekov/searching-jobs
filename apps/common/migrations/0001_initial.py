# Generated by Django 5.1.1 on 2024-09-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('social', models.CharField(choices=[('telegram', 'Telegram'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('youtube', 'Youtube')], max_length=16)),
                ('link', models.URLField()),
            ],
        ),
    ]