# Generated by Django 4.0 on 2021-12-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.TextField(),
        ),
    ]