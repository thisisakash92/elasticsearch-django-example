from elasticsearch_django.settings import get_client
from elasticsearch_dsl import Search
from django.http import JsonResponse
from django.conf import settings

def car_search(request):
    search = Search(using=get_client(), index=settings.ES_INDEX, doc_type='car')  # get es search instance
    query = search.query('wildcard', name='*{}*'.format(request.GET.get('key')))  # create query
    data = [r.to_dict() for r in query[:20].execute()]  # fetch result; limit results to 20 & convert to dicts
    return JsonResponse(data, safe=False)

