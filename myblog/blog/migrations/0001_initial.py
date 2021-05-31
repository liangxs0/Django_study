# Generated by Django 3.1.7 on 2021-04-09 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32, null=True, unique=True)),
                ('user_password', models.CharField(max_length=200, null=True)),
                ('user_describe', models.CharField(max_length=180)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_list',
            },
        ),
        migrations.CreateModel(
            name='FileList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_name', models.CharField(max_length=200, null=True)),
                ('File_content', models.CharField(max_length=200, null=True)),
                ('File_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userlist')),
            ],
            options={
                'db_table': 'file_list',
            },
        ),
    ]