# Generated by Django 3.0.3 on 2020-11-20 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=31)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'devices',
            },
        ),
        migrations.CreateModel(
            name='Microcontrollers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'microcontrollers',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth0_id', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=31)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Microcontrollers_Accounts',
            fields=[
                ('microcontroller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='smart_home.Microcontrollers')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_home.Accounts')),
            ],
            options={
                'db_table': 'microcontrollers_accounts',
            },
        ),
        migrations.CreateModel(
            name='Microcontroller_Devices',
            fields=[
                ('microcontroller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='smart_home.Microcontrollers')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_home.Devices')),
            ],
            options={
                'db_table': 'microcontroller_devices',
            },
        ),
        migrations.CreateModel(
            name='Account_Users',
            fields=[
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='smart_home.Accounts')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_home.Users')),
            ],
            options={
                'db_table': 'account_users',
            },
        ),
    ]