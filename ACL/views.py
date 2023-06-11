from django.conf import settings
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ACL.filters import PermissionFilters, RoleFilters, UserRoleFilters
from ACL.forms import RoleForm, PermissionForm, UserRoleForm
from ACL.models import *
from django.contrib.auth import get_user_model

from ACL.permissions import PERMISSIONS
from ACL.mixins import SuperUserRequiredMixin

User = get_user_model()


class RolesListView(SuperUserRequiredMixin, ListView):
    model = Role
    context_object_name = 'roles'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-updated_at']
    template_name = 'acl/admin/roles/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return RoleFilters(data=self.request.GET, queryset=queryset).qs


class RolesCreateView(SuperUserRequiredMixin, CreateView):
    model = Role
    template_name = 'acl/admin/roles/form.html'
    form_class = RoleForm
    success_url = reverse_lazy('roles-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['permissions'] = PERMISSIONS
        return context


class RolesUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'acl/admin/roles/form.html'
    success_url = reverse_lazy('roles-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['permissions'] = PERMISSIONS
        return context


class RolesDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Role
    template_name = 'acl/admin/roles/list.html'
    success_url = reverse_lazy('roles-list')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'نقش مورد نظر با موفقیت حدف شد.')
        return resp


###################################################################

class PermissionsListView(SuperUserRequiredMixin, ListView):
    model = Permission
    context_object_name = 'permissions'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-updated_at']
    template_name = 'acl/admin/permissions/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return PermissionFilters(data=self.request.GET, queryset=queryset).qs


class PermissionsCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "acl/admin/permissions/form.html"
    model = Permission
    form_class = PermissionForm
    success_url = reverse_lazy("permissions-list")


class PermissionsUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "acl/admin/permissions/form.html"
    model = Permission
    form_class = PermissionForm
    success_url = reverse_lazy("permissions-list")


class PermissionsDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Permission
    template_name = 'acl/admin/permissions/list.html'
    success_url = reverse_lazy("permissions-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'دسترسی مورد نظر با موفقیت حدف شد.')
        return resp


############################################################################

class RoleUserListView(SuperUserRequiredMixin, ListView):
    model = UserRole
    context_object_name = 'user_roles'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-updated_at']
    template_name = 'acl/admin/user_roles/list.html'
    queryset = UserRole.objects.filter(role__isnull=False)

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserRoleFilters(data=self.request.GET, queryset=queryset).qs


class RoleUserCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "acl/admin/user_roles/form.html"
    model = UserRole
    form_class = UserRoleForm
    success_url = reverse_lazy('role-user-list')

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('user'):
            try:
                User.objects.get(pk=self.request.GET.get('user'))
            except:
                raise Http404

        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return self.success_url


class RoleUserUpdateView(SuperUserRequiredMixin, UpdateView):
    model = UserRole
    form_class = UserRoleForm
    template_name = "acl/admin/user_roles/form.html"
    success_url = reverse_lazy('role-user-list')

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('user'):
            try:
                User.objects.get(pk=self.request.GET.get('user'))
            except:
                raise Http404

        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return self.success_url


class RoleUserDeleteView(SuperUserRequiredMixin, DeleteView):
    model = UserRole
    template_name = 'acl/admin/user_roles/list.html'
    success_url = reverse_lazy('role-user-list')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'کاربر مدیر مورد نظر با موفقیت حدف شد.')
        return resp
