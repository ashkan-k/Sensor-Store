# from Subscription.models import Type
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ACL.mixins import SuperUserRequiredMixin
from .filters import CategoryFilters
from .forms import CategoryForm
from .models import Category

""" Category """


class CategoryListView(SuperUserRequiredMixin, ListView):
    model = Category
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'categories/admin/categories/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return CategoryFilters(data=self.request.GET, queryset=queryset).qs


class CategoryCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "categories/admin/categories/form.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")


class CategoryUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "categories/admin/categories/form.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")


class CategoryDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/admin/categories/list.html'
    success_url = reverse_lazy("categories-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
