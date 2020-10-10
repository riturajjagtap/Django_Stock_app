from django.db import models

class StockTickers(models.Model):
    ticker = models.CharField(max_length=10)
    # company_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.ticker
