# Generated by Django 4.2.8 on 2023-12-20 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('phone_number', models.IntegerField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.accounttype')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district')),
                ('material_provided', models.ManyToManyField(to='bank.material')),
            ],
            options={
                'verbose_name': 'form',
                'verbose_name_plural': 'forms',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district'),
        ),
    ]
