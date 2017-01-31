from django.http import HttpResponse
from .models import GvData


def index(request):
    all_geneva = GvData.objects.all()
    html = ''

    for records in all_geneva:
        url = '/geneva/' + str(GvData.id) + '/'
        html += '<a href="' + url + '">title</a><br>'
    return HttpResponse(html)


def geneva_record(request, geneva_id):
    return HttpResponse('<h2> Details for specific record {}</h2>'.format(geneva_id))
