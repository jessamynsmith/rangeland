from django import forms
from django.contrib.auth.models import User
from .models import GvData


class GenevaForm(forms.ModelForm):
    class Meta:
        model = GvData
        fields = ['gv_01_close_gauge', 'gv_01_close_stock', 'gv_01_stock_change',
                  'gv_02_close_gauge', 'gv_02_close_stock', 'gv_02_stock_change',
                  'gv_03_close_gauge', 'gv_03_close_stock', 'gv_03_stock_change',
                  'tact1_close', 'tact1_total', 'tact2_close', 'tact2_total',
                  'tact3_close', 'tact3_total', 'tact4_close', 'tact4_total',
                  'tact5_close', 'tact5_total', 'incoming_meter_1_close',
                  'incoming_meter_1_total', 'incoming_meter_2_close',
                  'incoming_meter_2_total', 'incoming_meter_daily_total',
                  'outgoing_meter_1_close', 'outgoing_meter_1_total',
                  'outgoing_meter_2_close', 'outgoing_meter_2_total',
                  'outgoing_meter_daily_total', 'transactions_total', 'gsv_total',
                  'comments']
