# Generated by Django 2.2 on 2019-04-14 18:52

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('asker', '0006_auto_20190414_1848'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='Questions',
        ),
    ]