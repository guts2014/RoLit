from django.db import models

# Use lowercase table names to prevent bugs!
class Telemetry(models.Model):
    #id - primary key int
    report_datetime = models.DateTimeField('Report time', blank = False, null= False)
    battery = models.FloatField('Battery', blank=True, null=True)
    brake = models.FloatField('Brake', blank=True, null=True)
    coolant_t = models.FloatField('Coolant temperature', blank=True, null=True)
    fuel = models.FloatField('Fuel', blank=True, null=True)
    gear = models.FloatField('Gear', blank=True, null=True)
    map = models.FloatField('Manifold pressure', blank=True, null=True)
    mat = models.FloatField('Manifold temperature', blank=True, null=True)
    o2 = models.FloatField('Oxygen', blank=True, null=True)
    rpm = models.FloatField('RPM', blank=True, null=True)
    speed = models.FloatField('Speed', blank=True, null=True)
    throttle = models.FloatField('Throttle', blank=True, null=True)
    wheel_t_1 = models.FloatField('Wheel 1 temperature', blank=True, null=True)
    wheel_t_2 = models.FloatField('Wheel 2 temperature', blank=True, null=True)
    wheel_t_3 = models.FloatField('Wheel 3 temperature', blank=True, null=True)
    wheel_t_4 = models.FloatField('Wheel 4 temperature', blank=True, null=True)
    wheel_v_1 = models.FloatField('Wheel 1 velocity', blank=True, null=True)
    wheel_v_2 = models.FloatField('Wheel 2 velocity', blank=True, null=True)
    wheel_v_3 = models.FloatField('Wheel 3 velocity', blank=True, null=True)
    wheel_v_4 = models.FloatField('Wheel 4 velocity', blank=True, null=True)

    class Meta:
        db_table = 'telemetry'
