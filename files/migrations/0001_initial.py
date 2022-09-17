# Generated by Django 4.1 on 2022-09-11 22:10

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
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadfile', models.FileField(blank=True, upload_to='upload_files/%Y/%m/%d/', verbose_name='Files')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date_file')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Files',
                'verbose_name_plural': 'Files',
                'ordering': ['-created_at'],
            },
        ),
    ]