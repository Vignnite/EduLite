# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class All2019(models.Model):
    applnno = models.IntegerField(blank=True, null=True)
    cutoff = models.TextField(blank=True, null=True)
    genrank = models.IntegerField(blank=True, null=True)
    collegecode = models.IntegerField(blank=True, null=True)
    branchcode = models.TextField(blank=True, null=True)
    community = models.TextField(blank=True, null=True)
    allotedcategory = models.TextField(blank=True, null=True)
    collegename = models.TextField(blank=True, null=True)
    branchname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all2019'


class All2020(models.Model):
    applnno = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cutoff = models.TextField(blank=True, null=True)
    genrank = models.IntegerField(blank=True, null=True)
    collegecode = models.IntegerField(blank=True, null=True)
    branchcode = models.TextField(blank=True, null=True)
    community = models.TextField(blank=True, null=True)
    allotedcategory = models.TextField(blank=True, null=True)
    collegename = models.TextField(blank=True, null=True)
    branchname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all2020'


class All2021(models.Model):
    applnno = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cutoff = models.TextField(blank=True, null=True)
    genrank = models.IntegerField(blank=True, null=True)
    collegecode = models.IntegerField(blank=True, null=True)
    branchcode = models.TextField(blank=True, null=True)
    community = models.TextField(blank=True, null=True)
    allotedcategory = models.TextField(blank=True, null=True)
    collegename = models.TextField(blank=True, null=True)
    branchname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all2021'


class All2022(models.Model):
    applnno = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    cutoff = models.TextField(blank=True, null=True)
    genrank = models.IntegerField(blank=True, null=True)
    collegecode = models.IntegerField(blank=True, null=True)
    branchcode = models.TextField(blank=True, null=True)
    community = models.TextField(blank=True, null=True)
    allotedcategory = models.TextField(blank=True, null=True)
    collegename = models.TextField(blank=True, null=True)
    branchname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all2022'


class Allotment1922(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    # Field name made lowercase.
    applnno = models.BigIntegerField(
        db_column='ApplnNo', blank=True, null=True)
    # Field name made lowercase.
    cutoff = models.FloatField(db_column='CutOff', blank=True, null=True)
    # Field name made lowercase.
    genrank = models.BigIntegerField(
        db_column='GenRank', blank=True, null=True)
    # Field name made lowercase.
    collegecode = models.BigIntegerField(
        db_column='CollegeCode', blank=True, null=True)
    # Field name made lowercase.
    branchcode = models.TextField(
        db_column='BranchCode', blank=True, null=True)
    # Field name made lowercase.
    community = models.TextField(db_column='Community', blank=True, null=True)
    # Field name made lowercase.
    allotedcategory = models.TextField(
        db_column='AllotedCategory', blank=True, null=True)
    # Field name made lowercase.
    collegename = models.TextField(
        db_column='CollegeName', blank=True, null=True)
    # Field name made lowercase.
    branchname = models.TextField(
        db_column='BranchName', blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allotment_19_22'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CourseAndCodes(models.Model):
    # Field name made lowercase.
    branchname = models.TextField(
        db_column='BranchName', blank=True, null=True)
    # Field name made lowercase.
    branchcode = models.TextField(
        db_column='BranchCode', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_and_codes'


class Cutoff1922(models.Model):
    # Field name made lowercase.
    collegecode = models.BigIntegerField(
        db_column='CollegeCode', blank=True, null=True)
    # Field name made lowercase.
    branchcode = models.TextField(
        db_column='BranchCode', blank=True, null=True)
    # Field name made lowercase.
    community = models.TextField(db_column='Community', blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    # Field name made lowercase.
    mincutoff = models.FloatField(db_column='MinCutoff', blank=True, null=True)
    # Field name made lowercase.
    maxcutoff = models.FloatField(db_column='MaxCutoff', blank=True, null=True)
    ind = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cutoff_19_22'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FinalAllotments1922(models.Model):
    # Field name made lowercase.
    branchname = models.TextField(
        db_column='BranchName', blank=True, null=True)
    # Field name made lowercase.
    collegename = models.TextField(
        db_column='CollegeName', blank=True, null=True)
    # Field name made lowercase.
    collegecode = models.BigIntegerField(
        db_column='CollegeCode', blank=True, null=True)
    # Field name made lowercase.
    community = models.TextField(db_column='Community', blank=True, null=True)
    # Field name made lowercase.
    meancutoff = models.FloatField(
        db_column='MeanCutoff', blank=True, null=True)
    # Field name made lowercase.
    maxcutoff = models.FloatField(db_column='MaxCutoff', blank=True, null=True)
    # Field name made lowercase.
    mincutoff = models.FloatField(db_column='MinCutoff', blank=True, null=True)
    # Field name made lowercase.
    branchcode = models.TextField(
        db_column='BranchCode', blank=True, null=True)
    ind = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'final_allotments_19_22'


class MaxMinCutoff1922(models.Model):
    # Field name made lowercase.
    collegecode = models.BigIntegerField(
        db_column='CollegeCode', blank=True, null=True)
    # Field name made lowercase.
    collegename = models.TextField(
        db_column='CollegeName', blank=True, null=True)
    # Field name made lowercase.
    branchname = models.TextField(
        db_column='BranchName', blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    community = models.TextField(db_column='Community', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'max_min_cutoff_19_22'


class StandardCutoff1922(models.Model):
    # Field name made lowercase.
    collegename = models.TextField(
        db_column='CollegeName', blank=True, null=True)
    # Field name made lowercase.
    collegecode = models.BigIntegerField(
        db_column='CollegeCode', blank=True, null=True)
    # Field name made lowercase.
    meancutoff = models.FloatField(
        db_column='MeanCutoff', blank=True, null=True)
    # Field name made lowercase.
    branchname = models.TextField(
        db_column='BranchName', blank=True, null=True)
    # Field name made lowercase.
    community = models.TextField(db_column='Community', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_cutoff_19_22'


class T(models.Model):
    applnno = models.IntegerField(blank=True, null=True)
    cutoff = models.TextField(blank=True, null=True)
    genrank = models.IntegerField(blank=True, null=True)
    collegecode = models.IntegerField(blank=True, null=True)
    branchcode = models.TextField(blank=True, null=True)
    community = models.TextField(blank=True, null=True)
    allotedcategory = models.TextField(blank=True, null=True)
    collegename = models.TextField(blank=True, null=True)
    branchname = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't'


# class User(models.Model):
#     name = models.TextField(blank=True, null=False)
#     email = models.EmailField(blank=True, primary_key=True)
#     maths = models.FloatField(blank=True, null=False)
#     physics = models.FloatField(blank=True, null=False)
#     chemistry = models.FloatField(blank=True, null=False)

#     class Meta:
#         managed = False
#         db_table = 'user'
class Users(models.Model):
    name = models.TextField(blank=True, null=True)
    email = models.TextField(primary_key=True)
    maths = models.TextField()
    physics = models.TextField()
    chemistry = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'


class Collegenameoption(models.Model):
    # Field name made lowercase.
    collegename = models.TextField(
        db_column='CollegeName', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'collegenameoption'
