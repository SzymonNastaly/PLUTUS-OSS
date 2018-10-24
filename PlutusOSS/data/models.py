from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class Stock(models.Model):
    """Model to describe a single stock
    This is the main model of the app!
    """
    name = models.CharField(max_length=90, blank=False)
    ticker = models.CharField(max_length=10, blank=False)
    current_liab = models.BigIntegerField()
    equity = models.BigIntegerField()
    total_assets = models.BigIntegerField()
    revenue12 = models.BigIntegerField()
    revenue13 = models.BigIntegerField()
    revenue14 = models.BigIntegerField()
    revenue15 = models.BigIntegerField()
    revenue16 = models.BigIntegerField()
    ebit = models.BigIntegerField()
    netincome12 = models.BigIntegerField()
    netincome13 = models.BigIntegerField()
    netincome14 = models.BigIntegerField()
    netincome15 = models.BigIntegerField()
    netincome16 = models.BigIntegerField()
    free_cashflow = models.BigIntegerField()
    eps12 = models.FloatField()
    eps13 = models.FloatField()
    eps14 = models.FloatField()
    eps15 = models.FloatField()
    eps16 = models.FloatField()
    eps_e = models.FloatField()
    total_dividend = models.BigIntegerField()
    dividend_ps = models.FloatField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Creates token for authentication automatically with creation of user"""
    if created:
        Token.objects.create(user=instance)
