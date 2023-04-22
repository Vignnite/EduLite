# Generated by Django 4.0.3 on 2023-04-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edusol_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAndCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.TextField(blank=True, db_column='BranchName', null=True)),
                ('branchcode', models.TextField(blank=True, db_column='BranchCode', null=True)),
            ],
            options={
                'db_table': 'course_and_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalAllotments1922',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.TextField(blank=True, db_column='BranchName', null=True)),
                ('collegename', models.TextField(blank=True, db_column='CollegeName', null=True)),
                ('collegecode', models.BigIntegerField(blank=True, db_column='CollegeCode', null=True)),
                ('community', models.TextField(blank=True, db_column='Community', null=True)),
                ('meancutoff', models.FloatField(blank=True, db_column='MeanCutoff', null=True)),
                ('max', models.FloatField(blank=True, null=True)),
                ('min', models.FloatField(blank=True, null=True)),
                ('branchcode', models.TextField(blank=True, db_column='BranchCode', null=True)),
            ],
            options={
                'db_table': 'final_allotments_19_22',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaxMinCutoff1922',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegecode', models.BigIntegerField(blank=True, db_column='CollegeCode', null=True)),
                ('collegename', models.TextField(blank=True, db_column='CollegeName', null=True)),
                ('branchname', models.TextField(blank=True, db_column='BranchName', null=True)),
                ('max', models.FloatField(blank=True, null=True)),
                ('min', models.FloatField(blank=True, null=True)),
                ('community', models.TextField(blank=True, db_column='Community', null=True)),
            ],
            options={
                'db_table': 'max_min_cutoff_19_22',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StandardCutoff1922',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.TextField(blank=True, db_column='CollegeName', null=True)),
                ('collegecode', models.BigIntegerField(blank=True, db_column='CollegeCode', null=True)),
                ('meancutoff', models.FloatField(blank=True, db_column='MeanCutoff', null=True)),
                ('branchname', models.TextField(blank=True, db_column='BranchName', null=True)),
                ('community', models.TextField(blank=True, db_column='Community', null=True)),
            ],
            options={
                'db_table': 'standard_cutoff_19_22',
                'managed': False,
            },
        ),
    ]
