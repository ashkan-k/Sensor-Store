# from Subscription.models import Type
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ACL.mixins import SuperUserRequiredMixin
from .filters import ArticleFilters
from .forms import ArticleForm
from .models import Article

""" Article """


class ArticleListView(SuperUserRequiredMixin, ListView):
    model = Article
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'articles/admin/articles/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return ArticleFilters(data=self.request.GET, queryset=queryset).qs


class ArticleCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "articles/admin/articles/form.html"
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("articles-list")


class ArticleUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "articles/admin/articles/form.html"
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("articles-list")


class ArticleDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/admin/articles/list.html'
    success_url = reverse_lazy("articles-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
