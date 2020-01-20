# Generated by Django 2.2.3 on 2019-08-24 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shepherd', '0002_auto_20190726_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_status',
            field=models.ForeignKey(default=1, help_text="The domain's current status - set to Available in most cases, or set to Reserved if it should not be used yet", null=True, on_delete=django.db.models.deletion.PROTECT, to='shepherd.DomainStatus'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='health_status',
            field=models.ForeignKey(default=1, help_text="The domain's current health status - set to Healthy if you are not sure and assumed the domain is ready to be used", null=True, on_delete=django.db.models.deletion.PROTECT, to='shepherd.HealthStatus'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='whois_status',
            field=models.ForeignKey(default=1, help_text="The domain's WHOIS privacy status - you want this to be Enabled with your registrar", null=True, on_delete=django.db.models.deletion.PROTECT, to='shepherd.WhoisStatus'),
        ),
    ]
