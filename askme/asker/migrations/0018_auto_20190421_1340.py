# Generated by Django 2.2 on 2019-04-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0017_auto_20190421_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
