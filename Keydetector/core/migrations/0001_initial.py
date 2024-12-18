# Generated by Django 5.0.7 on 2024-11-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(blank=True, max_length=20)),
                ('alternative_key', models.CharField(blank=True, max_length=20, null=True)),
                ('correlation', models.FloatField(null=True)),
                ('alternative_correlation', models.FloatField(null=True)),
            ],
        ),
    ]
