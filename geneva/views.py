from django.shortcuts import render, get_object_or_404
from .models import GvData


def index(request):
    all_geneva_data = GvData.objects.all()
    return render(request, 'geneva/index.html', {'all_geneva_data': all_geneva_data})


def geneva_record(request, geneva_id):
    # try:
    #     record = GvData.objects.get(pk=geneva_id)
    # except GvData.DoesNotExist:
    #     raise Http404("Record does not exist")
    record = get_object_or_404(GvData, pk=geneva_id)
    return render(request, 'geneva/geneva_record.html', {'record': record})


def redirect(request, geneva_id):
    record = get_object_or_404(GvData, pk=geneva_id)
    try:
        pass
    except(KeyError, GvData.DoesNotExist):
        return render(request, 'geneva/geneva_record.html', {
            'record': record,
            'error_message': 'Invalid Selection'
        })
    else:
        return render(request, 'geneva/geneva_record.html', {'record': record})
