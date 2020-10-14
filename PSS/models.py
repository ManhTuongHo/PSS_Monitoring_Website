from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=500, blank = True, null=True)
    address = models.CharField(max_length=500, default=None, blank=True, null=True)
    start_year = models.IntegerField(null = True)
    start_month = models.IntegerField(null=True)

class Hub(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hub_name = models.CharField(max_length=100)


class Load(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    load_name = models.CharField(max_length=100)
    essential = models.BooleanField(default=True)


class Panel(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    panel_name = models.CharField(max_length=100, null=True)
    rated_power = models.FloatField(null=True)
    install_cost = models.FloatField(default=0.0)
    life_span = models.IntegerField(default=25)


class LoadStatus(models.Model):
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    consumption = models.FloatField(default=0.0)
    date_time = models.DateTimeField(auto_now_add=False, auto_now=False)


class PanelStatus(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    generation = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=False, auto_now=False)


class PowerExchange(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    energy_rate_system = models.FloatField(null=True)
    contrib = models.FloatField(null=True)
    consume = models.FloatField(null=True)
    contrib_amount_system = models.FloatField(null=True)
    consume_amount_system = models.FloatField(null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)


class PaymentStatus(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    earn_or_pay = models.BooleanField()
    amount = models.FloatField(null=True)
    pay_centre = models.FloatField(null = True)
    status = models.BooleanField(default = False)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)