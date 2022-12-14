# Generated by Django 4.0.6 on 2022-09-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('productid', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order_db',
            },
        ),
        migrations.CreateModel(
            name='profit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('earning', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'profit_db',
            },
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emailid', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'report_db',
            },
        ),
        migrations.CreateModel(
            name='storeproperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(default=None, max_length=100)),
                ('area', models.CharField(default=None, max_length=100)),
                ('landmark', models.CharField(default=None, max_length=100)),
                ('length', models.CharField(default=None, max_length=100)),
                ('width', models.CharField(default=None, max_length=100)),
                ('totalsqft', models.IntegerField()),
                ('image', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('description', models.CharField(max_length=500)),
                ('cat', models.CharField(default=None, max_length=20)),
                ('price', models.IntegerField()),
                ('opensides', models.CharField(default=None, max_length=100)),
                ('water', models.CharField(default=None, max_length=100)),
                ('electricity', models.CharField(default=None, max_length=100)),
                ('sewage', models.CharField(default=None, max_length=100)),
                ('road', models.CharField(default=None, max_length=100)),
                ('squarefeet', models.CharField(default=None, max_length=100)),
                ('bedroom', models.CharField(default=None, max_length=100)),
                ('bathroom', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'post_db',
            },
        ),
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'userdb',
            },
        ),
    ]
