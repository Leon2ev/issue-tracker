# Generated by Django 2.2.9 on 2020-01-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20200126_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='Pending', max_length=20),
        ),
    ]
