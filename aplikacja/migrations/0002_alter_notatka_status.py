# Generated by Django 5.0.6 on 2024-05-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notatka',
            name='status',
            field=models.CharField(choices=[('mniejwazne', 'Mniejwazne'), ('wazne', 'Wazne')], default='mniejwazne', max_length=10),
        ),
    ]
