# Generated by Django 2.2 on 2019-04-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=20)),
                ('Emain', models.CharField(max_length=20)),
                ('NickName', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=32)),
            ],
        ),
    ]