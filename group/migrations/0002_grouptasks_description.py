# Generated by Django 3.0.8 on 2020-09-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouptasks',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
