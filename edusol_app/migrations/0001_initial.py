# Generated by Django 4.0.3 on 2023-04-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All2019',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applnno', models.IntegerField(blank=True, null=True)),
                ('cutoff', models.TextField(blank=True, null=True)),
                ('genrank', models.IntegerField(blank=True, null=True)),
                ('collegecode', models.IntegerField(blank=True, null=True)),
                ('branchcode', models.TextField(blank=True, null=True)),
                ('community', models.TextField(blank=True, null=True)),
                ('allotedcategory', models.TextField(blank=True, null=True)),
                ('collegename', models.TextField(blank=True, null=True)),
                ('branchname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'all2019',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='All2020',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applnno', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('cutoff', models.TextField(blank=True, null=True)),
                ('genrank', models.IntegerField(blank=True, null=True)),
                ('collegecode', models.IntegerField(blank=True, null=True)),
                ('branchcode', models.TextField(blank=True, null=True)),
                ('community', models.TextField(blank=True, null=True)),
                ('allotedcategory', models.TextField(blank=True, null=True)),
                ('collegename', models.TextField(blank=True, null=True)),
                ('branchname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'all2020',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='All2021',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applnno', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('cutoff', models.TextField(blank=True, null=True)),
                ('genrank', models.IntegerField(blank=True, null=True)),
                ('collegecode', models.IntegerField(blank=True, null=True)),
                ('branchcode', models.TextField(blank=True, null=True)),
                ('community', models.TextField(blank=True, null=True)),
                ('allotedcategory', models.TextField(blank=True, null=True)),
                ('collegename', models.TextField(blank=True, null=True)),
                ('branchname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'all2021',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='All2022',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applnno', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('cutoff', models.TextField(blank=True, null=True)),
                ('genrank', models.IntegerField(blank=True, null=True)),
                ('collegecode', models.IntegerField(blank=True, null=True)),
                ('branchcode', models.TextField(blank=True, null=True)),
                ('community', models.TextField(blank=True, null=True)),
                ('allotedcategory', models.TextField(blank=True, null=True)),
                ('collegename', models.TextField(blank=True, null=True)),
                ('branchname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'all2022',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Allotment1922',
            fields=[
                ('index', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('applnno', models.BigIntegerField(blank=True, db_column='ApplnNo', null=True)),
                ('cutoff', models.FloatField(blank=True, db_column='CutOff', null=True)),
                ('genrank', models.BigIntegerField(blank=True, db_column='GenRank', null=True)),
                ('collegecode', models.BigIntegerField(blank=True, db_column='CollegeCode', null=True)),
                ('branchcode', models.TextField(blank=True, db_column='BranchCode', null=True)),
                ('community', models.TextField(blank=True, db_column='Community', null=True)),
                ('allotedcategory', models.TextField(blank=True, db_column='AllotedCategory', null=True)),
                ('collegename', models.TextField(blank=True, db_column='CollegeName', null=True)),
                ('branchname', models.TextField(blank=True, db_column='BranchName', null=True)),
                ('year', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'allotment_19_22',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cutoff1922',
            fields=[
                ('collegecode', models.BigIntegerField(blank=True, db_column='CollegeCode', null=True)),
                ('branchcode', models.TextField(blank=True, db_column='BranchCode', null=True)),
                ('community', models.TextField(blank=True, db_column='Community', null=True)),
                ('year', models.BigIntegerField(blank=True, null=True)),
                ('mincutoff', models.FloatField(blank=True, db_column='MinCutoff', null=True)),
                ('maxcutoff', models.FloatField(blank=True, db_column='MaxCutoff', null=True)),
                ('ind', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cutoff_19_22',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applnno', models.IntegerField(blank=True, null=True)),
                ('cutoff', models.TextField(blank=True, null=True)),
                ('genrank', models.IntegerField(blank=True, null=True)),
                ('collegecode', models.IntegerField(blank=True, null=True)),
                ('branchcode', models.TextField(blank=True, null=True)),
                ('community', models.TextField(blank=True, null=True)),
                ('allotedcategory', models.TextField(blank=True, null=True)),
                ('collegename', models.TextField(blank=True, null=True)),
                ('branchname', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't',
                'managed': False,
            },
        ),
    ]
