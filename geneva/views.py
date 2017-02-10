from django.views import generic
from .models import GvData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'geneva/index.html'

    def get_queryset(self):
        return GvData.objects.all()


class RecordView(generic.DetailView):
    model = GvData
    template_name = 'geneva/geneva_record.html'


class RecordCreate(CreateView):
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
              'comments', 'pub_date', 'report_file']

    def form_valid(self, form):
        form.instance.incoming_meter_daily_total = (form.instance.incoming_meter_1_total +
                                                    form.instance.incoming_meter_2_total)
        form.save()

        return HttpResponseRedirect('geneva:index')


class RecordUpdate(UpdateView):
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
              'comments', 'pub_date', 'report_file']


class RecordDelete(DeleteView):
    model = GvData
    success_url = reverse_lazy('geneva:index')

# def meter_variables(request):
#
#     incoming_meter_daily_total = (object.incoming_meter_1_close - object.incoming_meter_1_open)
#     + (object.incoming_meter_2_close - object.incoming_meter_2_close)
#
#     return (request, 'geneva/geneva_record.html',
#                   {'incoming_meter_daily_total': incoming_meter_daily_total})
