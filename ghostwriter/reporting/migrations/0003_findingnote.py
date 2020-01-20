# Generated by Django 2.2.3 on 2019-08-22 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reporting', '0002_localfindingnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindingNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True, help_text='Creation timestamp', max_length=100, verbose_name='Timestamp')),
                ('note', models.TextField(blank=True, help_text='Use this area to add a note to this finding - it can be anything you want others to see/know about the finding', null=True, verbose_name='Notes')),
                ('finding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.Finding')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Local finding note',
                'verbose_name_plural': 'Local finding notes',
                'ordering': ['finding', '-timestamp'],
            },
        ),
    ]
