from django.db import models
from django.core.urlresolvers import reverse


class GvData(models.Model):
    gv_01_open_stock = models.FloatField(default=0)
    gv_02_open_stock = models.FloatField(default=0)
    gv_03_open_stock = models.FloatField(default=0)
    gv_01_close_stock = models.FloatField(default=0)
    gv_02_close_stock = models.FloatField(default=0)
    gv_03_close_stock = models.FloatField(default=0)
    gv_01_open_gauge = models.CharField(max_length=20, default="0' 0\" /16ths")
    gv_02_open_gauge = models.CharField(max_length=20, default="0' 0\" /16ths")
    gv_03_open_gauge = models.CharField(max_length=20, default="0' 0\" /16ths")
    gv_01_close_gauge = models.CharField(max_length=20, default="0' 0\" /16ths")
    gv_02_close_gauge = models.CharField(max_length=20, default="0' 0\" /16ths")
    gv_03_close_gauge = models.CharField(max_length=20, default="0' 0\" /16ths")
    gv_01_stock_change = models.FloatField(default=0)
    gv_02_stock_change = models.FloatField(default=0)
    gv_03_stock_change = models.FloatField(default=0)
    tact1_open = models.FloatField(default=0)
    tact2_open = models.FloatField(default=0)
    tact3_open = models.FloatField(default=0)
    tact4_open = models.FloatField(default=0)
    tact5_open = models.FloatField(default=0)
    tact1_close = models.FloatField(default=0)
    tact2_close = models.FloatField(default=0)
    tact3_close = models.FloatField(default=0)
    tact4_close = models.FloatField(default=0)
    tact5_close = models.FloatField(default=0)
    tact1_total = models.FloatField(default=0)
    tact2_total = models.FloatField(default=0)
    tact3_total = models.FloatField(default=0)
    tact4_total = models.FloatField(default=0)
    tact5_total = models.FloatField(default=0)
    incoming_meter_1_open = models.FloatField(default=0)
    incoming_meter_2_open = models.FloatField(default=0)
    incoming_meter_1_close = models.FloatField(default=0)
    incoming_meter_2_close = models.FloatField(default=0)
    outgoing_meter_1_open = models.FloatField(default=0)
    outgoing_meter_2_open = models.FloatField(default=0)
    outgoing_meter_1_close = models.FloatField(default=0)
    outgoing_meter_2_close = models.FloatField(default=0)
    incoming_meter_1_total = models.FloatField(default=0)
    incoming_meter_2_total = models.FloatField(default=0)
    outgoing_meter_1_total = models.FloatField(default=0)
    outgoing_meter_2_total = models.FloatField(default=0)
    incoming_meter_daily_total = models.FloatField(default=0)
    outgoing_meter_daily_total = models.FloatField(default=0)
    gsv_total = models.FloatField(default=0)
    transactions_total = models.FloatField(default=0)
    comments = models.CharField(max_length=200, default='comments')
    slug = models.SlugField(unique=True)
    report_file = models.FileField(default=None)
    pub_date = models.DateField(db_index=True)

    def __str__(self):
        return str(self.pub_date) + '(' + str(self.pk) + ')'

    def get_absolute_url(self):
        return reverse('geneva:geneva', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'GV info'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
