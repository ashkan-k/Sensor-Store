from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.views.generic import TemplateView

from ACL.mixins import VerifiedUserMixin
from Payment.models import Payment
from Category.models import Category

User = get_user_model()


###############################################

class Dashboard(VerifiedUserMixin, TemplateView):
    template_name = "admin_app/admin/admin-dashboard.html"

    def get_context_data(self, **kwargs):
        context = {
            'total_transaction_amount':
                Payment.objects.filter(status=True).aggregate(total_amount=Sum('amount'))[
                    'total_amount'],
            'users_count': User.objects.count(),
            'categories': Category.objects.filter().order_by('-id')[:5],
        }

        return context
