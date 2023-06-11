from django.contrib.auth.forms import SetPasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView as LoginViewAuto
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from ACL.mixins import AnonymousUserMixin, CheckPasswordResetExpirationMixin
from .forms import *
from .mixins import CheckTeacherStatusMixin
from unidecode import unidecode


class RegisterView(AnonymousUserMixin, CreateView):
    template_name = "auth/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("verify-code")

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['phone'] = unidecode(request.POST.get('phone'))
        request.POST['national_id'] = unidecode(request.POST.get('national_id'))
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class LoginView(CheckTeacherStatusMixin, LoginViewAuto):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('index')
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['username'] = unidecode(request.POST.get('username'))
        return super().post(request, *args, **kwargs)


class ResetPasswordView(AnonymousUserMixin, CreateView):
    template_name = "auth/reset_password/form.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy("password-reset-confirm")

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['phone'] = unidecode(request.POST.get('phone'))
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class ResetPasswordEnterView(AnonymousUserMixin, CheckPasswordResetExpirationMixin, CreateView):
    template_name = "auth/reset_password/form.html"
    form_class = SetPasswordForm
    success_url = reverse_lazy("login")

    def get_current_user(self):
        code = get_object_or_404(Code, code=self.request.session['reset_password_code'])
        user = get_object_or_404(User, pk=code.user_id)
        return user

    def get(self, req):
        user = self.get_current_user()
        return render(req, self.template_name, {"form": self.form_class(user)})

    def post(self, req):
        user = self.get_current_user()
        form = SetPasswordForm(user, req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'رمزعبور با موفقیت بازیابی شد. اکنون میتوانید با رمز عبور جدید وارد شوید.')
            return redirect(self.success_url)
        return render(req, self.template_name, context={"form": form})


class VerifyCodeView(AnonymousUserMixin, FormView):
    template_name = "auth/verify_code.html"
    form_class = CodeForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.save(True)

        if resolve(self.request.path_info).url_name == 'password-reset-confirm':
            return HttpResponseRedirect(reverse_lazy('password-reset-enter'))

        if self.request.user.role_code == 'student':
            return HttpResponseRedirect(reverse_lazy("student-profile"))
        elif self.request.user.role_code == 'teacher':
            return HttpResponseRedirect(reverse_lazy("teacher-profile"))
        elif self.request.user.role_code == 'teacher':
            return HttpResponseRedirect(reverse_lazy("dashboard"))

        return HttpResponseRedirect(reverse_lazy("dashboard"))
