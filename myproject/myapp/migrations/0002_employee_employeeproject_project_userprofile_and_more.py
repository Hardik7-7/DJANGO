# Generated by Django 5.0.7 on 2024-07-27 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('estimated_span', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='employeeproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='employeeproject',
            unique_together={('employee', 'project')},
        ),
    ]
