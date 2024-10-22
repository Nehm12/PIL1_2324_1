# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Interest(models.Model):
    gender = models.CharField(max_length=1)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    localisation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interest'


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    user1 = models.OneToOneField('User', models.DO_NOTHING)
    user2 = models.OneToOneField('User', models.DO_NOTHING)
    content = models.CharField(max_length=255, blank=True, null=True)
    heure = models.TimeField(blank=True, null=True)
    jour = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Profile(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    bio = models.CharField(max_length=100, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    age = models.IntegerField()
    location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'profile'


class ProfileInterests(models.Model):
    profile = models.OneToOneField(Profile, models.DO_NOTHING, primary_key=True)
    interest = models.ForeignKey(Interest, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_interests'
        unique_together = (('profile', 'interest'),)


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user'
