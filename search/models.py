from django.db import models
from elasticsearch_django.models import SearchDocumentMixin, SearchDocumentManagerMixin


class ElasticManager(models.Manager, SearchDocumentManagerMixin):
    def get_search_queryset(self, index='_all'):
        return self.get_queryset()

class Car(models.Model, SearchDocumentMixin):
    model_name = models.CharField(max_length=30)
    year = models.IntegerField()
    objects = ElasticManager()

    def as_search_document(self, index='_all'):
        return {'name': self.model_name, 'year': self.year, 'id': self.id}

