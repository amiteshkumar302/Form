from django.db import models


# Create your models here.
class Vechicle(models.Model):
    SAP_Code = models.CharField(max_length=30)
    Ledger_Name = models.CharField(max_length=10)
    Manufacturer = models.CharField(max_length=12)
    Model = models.CharField(max_length=20)
    Vehicle_Type = models.CharField(max_length=5)
    Base_Km = models.IntegerField()
    RTO = models.CharField(max_length=50)
    class Meta:
        db_table = "Vehicle"


class Engine(models.Model):
    Model_year = models.CharField(max_length=20)
    Chassis_No =models.CharField(max_length=60)
    Fuel_TYPE = models.CharField(max_length=20)
    old_vehicle_No = models.CharField(max_length=30)
    class Meta:
        db_table = "Engine"