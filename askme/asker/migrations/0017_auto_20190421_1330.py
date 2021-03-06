# Generated by Django 2.2 on 2019-04-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0016_auto_20190421_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(db_index=True, max_length=128),
        ),
    ]
