# Generated by Django 2.2 on 2019-04-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=64)),
                ('Text', models.TextField()),
                ('Autor', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
