from django import forms


class CheckTeacherStatusMixin:
    def form_valid(self, form):
        user = form.get_user()
        if user.role_code == 'teacher' and not user.teacher_profile.is_approved:
            raise forms.ValidationError(
                'ثبت نام شما با موفقیت انجام شده است ولی حساب کاربری شما توسط مدیر هنوز تایید نشده است.')

        return super().form_valid(form)
