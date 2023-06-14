from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from ACL.mixins import SuperUserRequiredMixin
from Permission.admin import IsAdminMixin
from config.pagination import CustomPagination
from django.utils.translation import gettext_lazy as _
from .models import *
from .serializer import *

""" Payment """


class PaymentListView(SuperUserRequiredMixin, ListView):
    model = Payment
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'payments/admin/payments/list.html'


class PaymentDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Payment
    template_name = 'payments/admin/payments/list.html'
    success_url = reverse_lazy("payments-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
