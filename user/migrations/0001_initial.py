# Generated by Django 4.0 on 2021-12-12 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatchTable',
            fields=[
                ('M_Id', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Edit', models.BooleanField()),
                ('Delete', models.BooleanField()),
                ('Add', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Surname', models.CharField(max_length=120)),
                ('Username', models.CharField(max_length=120)),
                ('Gender', models.CharField(max_length=120)),
                ('Birthday', models.DateField()),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=120)),
                ('Password', models.CharField(max_length=500)),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='user.role')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.TextField()),
                ('Date', models.DateField()),
                ('M_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchtables', to='user.matchtable')),
                ('WhoSend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users3', to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='matchtable',
            name='OU_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users2', to='user.user'),
        ),
        migrations.AddField(
            model_name='matchtable',
            name='U_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users1', to='user.user'),
        ),
    ]
