# Generated by Django 4.0 on 2022-01-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_matchtable_productimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchtable',
            name='ProductName',
            field=models.CharField(default='', max_length=1200),
        ),
    ]
