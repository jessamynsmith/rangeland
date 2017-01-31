from django.http import Http404
from django.shortcuts import render
from .models import GvData


def index(request):
    all_geneva_data = GvData.objects.all()
    return render(request, 'geneva/index.html', {'all_geneva_data': all_geneva_data})


def geneva_record(request, geneva_id):
    try:
        record = GvData.objects.get(pk=geneva_id)
    except GvData.DoesNotExist:
        raise Http404("Record does not exist")
    return render(request, 'geneva/geneva_record.html', {'record': record})
