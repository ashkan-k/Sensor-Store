""" Cart """
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from ACL.mixins import SuperUserRequiredMixin
from Cart.forms import CartForm
from Cart.models import Cart

""" Cart """


class CartListView(SuperUserRequiredMixin, ListView):
    model = Cart
    context_object_name = 'suggestions'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'carts/admin/carts/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return CartFilters(data=self.request.GET, queryset=queryset).qs


class CartDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Cart
    template_name = 'carts/admin/carts/list.html'
    success_url = reverse_lazy("carts-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Front Side """


class CartView(CreateView):
    template_name = "carts/front/cart_form.html"
    model = Cart
    form_class = CartForm
    success_url = reverse_lazy("carts-add")

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد.')
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
