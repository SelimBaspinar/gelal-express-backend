# Generated by Django 4.0 on 2021-12-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_matchtable_makedeal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchtable',
            old_name='MakeDeal',
            new_name='MakeDealOU',
        ),
        migrations.AddField(
            model_name='matchtable',
            name='MakeDealU',
            field=models.BooleanField(default=False),
        ),
    ]