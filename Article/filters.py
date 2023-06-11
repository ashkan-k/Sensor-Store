import django_filters as filters
from django.db.models import Q
from unidecode import unidecode


class ArticleFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    category = filters.CharFilter(method="category_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(title__icontains=value) |
            Q(body__icontains=value) |
            Q(author__first_name___icontains=value) |
            Q(author__last_name___icontains=value) |
            Q(author__username___icontains=value) |
            Q(author__phone___icontains=value) |
            Q(category__name__icontains=value) |
            Q(category__slug__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def category_filter(qs, name, value):
        qs = qs.filter(
            Q(category_id=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs
