# Generated by Django 2.2.3 on 2019-10-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shepherd', '0004_auto_20190910_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverhistory',
            name='activity_type',
            field=models.ForeignKey(help_text='Select the intended activity to be performed by the server', on_delete=django.db.models.deletion.PROTECT, to='shepherd.ActivityType'),
        ),
        migrations.AlterField(
            model_name='serverhistory',
            name='server_role',
            field=models.ForeignKey(help_text='Select the intended role the server will play', on_delete=django.db.models.deletion.PROTECT, to='shepherd.ServerRole'),
        ),
    ]
