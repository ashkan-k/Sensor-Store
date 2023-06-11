import django_filters as filters
from django.db.models import Q
from unidecode import unidecode


class CategoryFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    parent = filters.CharFilter(method="parent_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(name__icontains=value) |
            Q(slug__icontains=value) |
            Q(parent__name__icontains=value) |
            Q(parent__slug__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def parent_filter(qs, name, value):
        qs = qs.filter(
            Q(parent_id=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs
