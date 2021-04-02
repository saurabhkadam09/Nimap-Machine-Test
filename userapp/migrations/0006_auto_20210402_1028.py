# Generated by Django 3.1.5 on 2021-04-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_tbl_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_project',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tbl_project',
            name='created_by',
            field=models.CharField(default='admin', max_length=255),
        ),
    ]
