# Generated by Django 4.0 on 2022-01-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_matchtable_makedealou_matchtable_makedealu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchtable',
            name='ProductImg',
            field=models.ImageField(default='', upload_to='product_images'),
            preserve_default=False,
        ),
    ]