from django.http import HttpResponse
from .models import GvData


def index(request):
    html = ''

    return HttpResponse('<h1>This is the Geneva Home page</h1>')


def geneva_record(request, geneva_id):
    return HttpResponse('<h2> Details for specific record {}</h2>'.format(geneva_id))
