from django.http import HttpResponse
from .models import GvData


def index(request):
    all_geneva_data = GvData.objects.all()
    html = ''

    for record in all_geneva_data:
        url = '/geneva/{}/'.format(record.id)
        html += '<a href="{}">{}</a><br>'.format(url, record.pub_date)
    return HttpResponse(html)


def geneva_record(request, geneva_id):
    return HttpResponse('<h2> Details for specific record {}</h2>'.format(geneva_id))