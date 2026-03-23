# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class CaseAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    fk_report_id = models.IntegerField()
    fk_invest_id = models.IntegerField()
    assigned_at = models.DateField()
    assigned_status = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'case_assignment'


class CrimeCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_dec = models.TextField()

    class Meta:
        managed = False
        db_table = 'crime_category'


class CrimeEvidence(models.Model):
    crime_evidence_id = models.AutoField(primary_key=True)
    fk_crime_report_id = models.IntegerField()
    evidence_file_name = models.CharField(max_length=100)
    evidence_file_type = models.CharField(max_length=50)
    evidence_file = models.CharField(max_length=100)
    evidence_uploaded_date = models.DateField()
    fk_crime_user_id = models.IntegerField()
    uploaded_by = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'crime_evidence'


class CrimeLaw(models.Model):
    crime_law_id = models.AutoField(primary_key=True)
    fk_crime_cat_id = models.IntegerField()
    crime_law = models.TextField()

    class Meta:
        managed = False
        db_table = 'crime_law'


class CrimeReports(models.Model):
    crime_report_id = models.AutoField(primary_key=True)
    fk_user_id = models.IntegerField()
    fk_category_id = models.IntegerField()
    crime_report_title = models.CharField(max_length=100)
    crime_description = models.TextField()
    crime_report_location = models.CharField(max_length=50)
    crime_report_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    crime_report_longitude = models.DecimalField(max_digits=10, decimal_places=7)
    crime_report_date = models.DateField()
    crime_report_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'crime_reports'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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


class InvestigationNotes(models.Model):
    investigation_note_id = models.AutoField(primary_key=True)
    fk_report_id_notes = models.IntegerField()
    fk_notes_officer_id = models.IntegerField()
    investigation_note = models.TextField()
    note_created_date = models.DateField()
    investigation_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'investigation_notes'


class Investigator(models.Model):
    inv_id = models.AutoField(primary_key=True)
    inv_full_name = models.CharField(max_length=50)
    inv_email = models.CharField(max_length=100)
    inv_phone = models.CharField(max_length=10)
    inv_address = models.TextField()
    inv_location = models.CharField(max_length=50)
    inv_gender = models.CharField(max_length=20)
    inv_role = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'investigator'


class Login(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=10)
    user_address = models.TextField()
    user_location = models.CharField(max_length=50)
    user_gender = models.CharField(max_length=15)
    user_role = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'users'
