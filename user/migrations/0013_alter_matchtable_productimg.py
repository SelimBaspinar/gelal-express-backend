# Generated by Django 4.0 on 2022-01-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_matchtable_productimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchtable',
            name='ProductImg',
            field=models.CharField(default='', max_length=1200),
        ),
    ]
