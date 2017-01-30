from django.db import models


class Report(models.Model):
    gv_01_open = models.FloatField()
    gv_02_open = models.FloatField()
    gv_03_open = models.FloatField()
    gv_01_close = models.FloatField()
    gv_02_close = models.FloatField()
    gv_03_close = models.FloatField()
    pub_date = models.DateField()
    pass
