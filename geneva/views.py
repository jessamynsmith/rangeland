from django.http import HttpResponse
from django.template import loader
from .models import GvData


def index(request):
    all_geneva_data = GvData.objects.all()
    template = loader.get.template('')
    return HttpResponse('')


def geneva_record(request, geneva_id):
    return HttpResponse('<h2> Details for specific record {}</h2>'.format(geneva_id))