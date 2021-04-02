# Generated by Django 3.1.5 on 2021-04-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('created_at', models.TimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_client',
            },
        ),
    ]
