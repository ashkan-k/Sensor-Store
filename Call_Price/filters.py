import django_filters as filters
from django.db.models import Q
from unidecode import unidecode


class CallPriceFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(full_name__icontains=value) |
            Q(company_name__icontains=value) |
            Q(product__title__icontains=value) |
            Q(category__name__icontains=value) |
            Q(category__slug__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs
