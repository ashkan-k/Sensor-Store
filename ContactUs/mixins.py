class FilterSuggestionsQuerysetMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.user.is_staff:
            queryset = queryset.filter(user=self.user)
        return queryset
