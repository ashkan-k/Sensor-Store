# from Subscription.models import Type
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ACL.mixins import SuperUserRequiredMixin
from .filters import CouponFilters
from .forms import CouponForm
from .models import Coupon

""" Coupon """


class CouponListView(SuperUserRequiredMixin, ListView):
    model = Coupon
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'coupons/admin/coupons/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return CouponFilters(data=self.request.GET, queryset=queryset).qs


class CouponCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "coupons/admin/coupons/form.html"
    model = Coupon
    form_class = CouponForm
    success_url = reverse_lazy("coupons-list")


class CouponUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "coupons/admin/coupons/form.html"
    model = Coupon
    form_class = CouponForm
    success_url = reverse_lazy("coupons-list")


class CouponDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Coupon
    template_name = 'coupons/admin/coupons/list.html'
    success_url = reverse_lazy("coupons-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
