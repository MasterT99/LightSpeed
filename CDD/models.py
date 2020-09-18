
from django.db import models
# Create your models here.
# DO NOT TOUCH ANYTHING WITHOUT MY PERMISSION


class User(models.Model):
    fname = models.CharField(max_length=32, null=False)
    mname = models.CharField(max_length=32, null=False)
    lname = models.CharField(max_length=32, null=False)
    gender = models.CharField(max_length=6, null=False)
    degree = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=64, primary_key=True)
    password = models.CharField(max_length=8, null=False)
    total_claims = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = "user"


class Circular(models.Model):
    year = models.IntegerField(null=False)
    month = models.IntegerField(null=False)
    field = models.CharField(max_length=16, null=False)
    invention = models.CharField(max_length=10240, null=False)

    class Meta:
        db_table = "circular"


class Chat(models.Model):
    sender = models.CharField(max_length=64, null=False)
    receiver = models.CharField(max_length=64, null=False)
    message = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "chat"


class Claims(models.Model):
    email = models.EmailField(max_length=64, null=False)

    accident_date = models.DateField(null=False)
    accident_front = models.CharField(max_length=128, null=False)
    accident_rear = models.CharField(max_length=128, null=False)
    accident_left = models.CharField(max_length=128, null=False)
    accident_right = models.CharField(max_length=128, null=False)

    message = models.CharField(max_length=10240, null=False)
    processed = models.CharField(max_length=8, null=False, default="Pending")
    total_cost_estimation = models.IntegerField(default=0, null=True)

    bool_is_car = models.NullBooleanField(default=None, null=True)

    bool_hood = models.NullBooleanField(default=None, null=True)
    bool_boot = models.NullBooleanField(default=None, null=True)
    bool_bumper_front = models.NullBooleanField(default=None, null=True)
    bool_bumper_rear = models.NullBooleanField(default=None, null=True)
    bool_windshield_front = models.NullBooleanField(default=None, null=True)
    bool_windshield_rear = models.NullBooleanField(default=None, null=True)
    bool_door_left = models.NullBooleanField(default=None, null=True)
    bool_door_right = models.NullBooleanField(default=None, null=True)
    bool_window_left = models.NullBooleanField(default=None, null=True)
    bool_window_right = models.NullBooleanField(default=None, null=True)

    class Meta:
        db_table = "claims"


class PartCost(models.Model):
    make = models.CharField(max_length=32, primary_key=True) # TATA, Hyundai, Nissan, AUDI
    hood = models.IntegerField()
    boot = models.IntegerField()
    bumper = models.IntegerField()
    windshield = models.IntegerField()
    door = models.IntegerField()
    window = models.IntegerField()
    # light = models.IntegerField()
    # roof = models.IntegerField()
    # sideglass = models.IntegerField()

    class Meta:
        db_table = "partcost"


# Yours faithfully...
# have you read this??
