import os

from django.contrib.auth.forms import SetPasswordForm
from unidecode import unidecode
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import pandas as pd
# from Subscription.models import Type
from ACL.mixins import SuperUserRequiredMixin, VerifiedUserMixin, PermissionMixin
from .filters import UserFilters
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.views import View
from django.shortcuts import get_object_or_404
from django.conf import settings


class UsersListView(PermissionMixin, ListView):
    permissions = ['user_list']
    model = User
    context_object_name = 'users'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-date_joined']
    template_name = 'users/admin/users/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types_filter_items'] = [{"name": i[1], "id": i[0]} for i in
                                          (('user', 'کاربران'), ('student', 'هنرجویان'), ('teacher', 'مدرسان'))]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserFilters(data=self.request.GET, queryset=queryset).qs


class UsersCreateView(PermissionMixin, CreateView):
    permissions = ['user_create']
    template_name = "users/admin/users/form.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users-list")


class UsersUpdateView(PermissionMixin, UpdateView):
    permissions = ['user_edit']
    template_name = "users/admin/users/form.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users-list")


class UsersDeleteView(PermissionMixin, DeleteView):
    permissions = ['user_delete']
    model = User
    template_name = 'users/admin/users/list.html'
    success_url = reverse_lazy("users-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


##############################################################################

class UserChangePasswordView(PermissionMixin, View):
    permissions = ['user_change_password']
    form = SetPasswordForm
    template_name = 'users/admin/users/change_password.html'
    success_url = reverse_lazy("users-list")

    def get(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        context = {"form": self.form(user), 'object': user}
        return render(req, self.template_name, context)

    def post(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        form = self.form(user, req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'رمزعبور با موفقیت تغییر داده شد.')
            return redirect(self.success_url)
        return render(req, self.template_name, context={"form": form})


##############################################################################


class ChangePasswordView(VerifiedUserMixin, View):
    form = SetPasswordForm
    template_name = 'users/admin/users/change_password.html'
    success_url = reverse_lazy("dashboard")

    def get(self, req):
        context = {"form": self.form(req.user), 'object': req.user}
        return render(req, self.template_name, context)

    def post(self, req):
        form = SetPasswordForm(req.user, req.POST)
        if form.is_valid():
            user = form.save()
            messages.success(req, 'رمزعبور با موفقیت تغییر داده شد.')
            return redirect(self.success_url)
        return render(req, self.template_name, context={"form": form})


class ChangeAvatarView(VerifiedUserMixin, UpdateView):
    template_name = "users/admin/users/form.html"
    model = User
    fields = ['avatar']
    success_url = reverse_lazy("dashboard")

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(VerifiedUserMixin, UpdateView):
    template_name = "users/admin/users/form.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'phone', 'avatar']
    success_url = reverse_lazy("profile")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['phone'].widget.attrs['readonly'] = True
        form.fields['username'].widget.attrs['readonly'] = True
        return form

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['username'] = request.user.username
        request.POST['phone'] = request.user.phone
        messages.success(request, 'اطلاعات شما با موفقیت ویرایش شد.')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

##############################################################################

# class UsersExportExcelView(View):
#     def get(self, request):
#         file_folder = 'media/exports'
#         file_name = file_folder + '/UserPhonesExcel.xlsx'
#         if not os.path.exists(file_folder):
#             os.mkdir(file_folder)
#
#         users = []
#         for item in User.objects.values_list('phone', flat=True):
#             users.append(unidecode(item[1:]))
#
#         users_df_data = pd.DataFrame({
#             'Phones': users
#         })
#
#         users_df_data.to_excel(file_name)
#
#         return FileResponse(open(file_name, 'rb'), as_attachment=True)
