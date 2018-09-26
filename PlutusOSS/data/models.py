from django.db import models

#TODO Create validators (minimal value, etc.)

class Stock(models.Model):
    """Model to describe a single stock
    This is the main model of the app!
    """
    name = models.CharField(max_length=30, blank=False)
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
    eps12 = models.FloatField() #TODO: FloatField or DecimalField?
    eps13 = models.FloatField()
    eps14 = models.FloatField()
    eps15 = models.FloatField()
    eps16 = models.FloatField()
    eps_e = models.FloatField()
    total_dividend = models.BigIntegerField()
    dividend_ps = models.FloatField()
#    dividend_ps = models.DecimalField(max_digits=8, decimal_places=2)

