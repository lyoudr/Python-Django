# Generated by Django 3.0.7 on 2020-06-22 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('img_src', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255, unique=True)),
                ('job', models.CharField(default='F2E', max_length=255)),
                ('hobby', models.CharField(default='piano', max_length=255)),
                ('guide', models.CharField(default='Hello', max_length=255)),
                ('gender', models.CharField(default='girl', max_length=255)),
                ('country', models.CharField(default='Taiwan', max_length=255)),
                ('position', models.CharField(default='/home/ann/Code/React/Photos/Ann.jpg', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ShopItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('buyer', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('shoplists', models.ManyToManyField(to='piano.ShopList')),
                ('users', models.ManyToManyField(to='piano.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Chat_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_receive', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('who_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='piano.Users')),
            ],
        ),
    ]
