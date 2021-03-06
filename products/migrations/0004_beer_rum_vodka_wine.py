# Generated by Django 2.0.2 on 2018-11-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181115_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='rum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vodka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
    ]
