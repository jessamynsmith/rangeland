from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import GvData
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# def index(request):
#     all_geneva_data = GvData.objects.all()
#     return render(request, 'geneva/index.html', {'all_geneva_data': all_geneva_data})
#
#
# def geneva_record(request, geneva_id):
#
#     record = get_object_or_404(GvData, pk=geneva_id)
#     return render(request, 'geneva/geneva_record.html', {'record': record})


class IndexView(generic.ListView):
    template_name = 'geneva/index.html'

    def get_queryset(self):
        return GvData.objects.all()


class RecordView(generic.DetailView):
    model = GvData
    template_name = 'geneva/geneva_record.html'
