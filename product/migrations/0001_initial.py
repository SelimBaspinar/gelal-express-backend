# Generated by Django 4.0 on 2021-12-19 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Id', models.CharField(max_length=120)),
                ('Name', models.CharField(max_length=120)),
                ('Description', models.CharField(max_length=600)),
                ('Date', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='product_images')),
                ('Phone', models.IntegerField()),
                ('User', models.CharField(max_length=120)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.subcategory')),
            ],
        ),
    ]