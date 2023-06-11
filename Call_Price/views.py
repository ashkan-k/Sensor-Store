# from Subscription.models import Type
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ACL.mixins import SuperUserRequiredMixin, VerifiedUserMixin
from .filters import CallPriceFilters
from .forms import CallPriceForm
from .models import CallPrice

""" CallPrice """


class CallPriceListView(SuperUserRequiredMixin, ListView):
    model = CallPrice
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'callprices/admin/callprices/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return CallPriceFilters(data=self.request.GET, queryset=queryset).qs


class CallPriceCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "callprices/admin/callprices/form.html"
    model = CallPrice
    form_class = CallPriceForm
    success_url = reverse_lazy("callprices-list")


class CallPriceUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "callprices/admin/callprices/form.html"
    model = CallPrice
    form_class = CallPriceForm
    success_url = reverse_lazy("callprices-list")


class CallPriceDeleteView(SuperUserRequiredMixin, DeleteView):
    model = CallPrice
    template_name = 'callprices/admin/callprices/list.html'
    success_url = reverse_lazy("callprices-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Front """


class CallPriceCreateFrontView(VerifiedUserMixin, CreateView):
    template_name = "callprices/front/form.html"
    model = CallPrice
    form_class = CallPriceForm
    success_url = reverse_lazy("index")
