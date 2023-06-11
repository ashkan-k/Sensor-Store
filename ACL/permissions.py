PERMISSIONS = []

USERS_PERMISSIONS = {
    'title': 'دسترسی کاربران',
    'permissions': [
        {'name': 'لیست کاربران', 'code': 'user_list', 'description': 'دسترسی لیست کاربران'},
        {'name': 'افزودن کاربر', 'code': 'user_create', 'description': 'دسترسی ساخت کاربر جدید'},
        {'name': 'ویرایش کاربر', 'code': 'user_edit', 'description': 'دسترسی ویرایش کاربران'},
        {'name': 'حذف کاربر', 'code': 'user_delete', 'description': 'دسترسی حذف کاربران'},
        {'name': 'تغییر رمز عبور کاربر', 'code': 'user_change_password',
         'description': 'دسترسی تغییر رمز عبور کاربران'},
    ]
}
PERMISSIONS.append(USERS_PERMISSIONS)

######################################################################

ROLES_PERMISSIONS = {
    'title': 'دسترسی نقش ها',
    'permissions': [
        {'name': 'لیست نقش ها', 'code': 'role_list', 'description': 'دسترسی لیست نقش ها'},
        {'name': 'افزودن نقش', 'code': 'role_create', 'description': 'دسترسی ساخت نقش جدید'},
        {'name': 'ویرایش نقش', 'code': 'role_edit', 'description': 'دسترسی ویرایش نقش ها'},
        {'name': 'حذف نقش', 'code': 'role_delete', 'description': 'دسترسی حذف نقش ها'},
    ]
}
PERMISSIONS.append(ROLES_PERMISSIONS)

######################################################################

CLASS_PERMISSIONS = {
    'title': 'دسترسی کلاس ها',
    'permissions': [
        {'name': 'لیست کلاس ها', 'code': 'class_list', 'description': 'دسترسی لیست کلاس ها'},
        {'name': 'افزودن کلاس', 'code': 'class_create', 'description': 'دسترسی ساخت کلاس جدید'},
        {'name': 'ویرایش کلاس', 'code': 'class_edit', 'description': 'دسترسی ویرایش کلاس ها'},
        {'name': 'حذف کلاس', 'code': 'class_delete', 'description': 'دسترسی حذف کلاس ها'},
        {'name': 'جزییات کلاس', 'code': 'class_detail', 'description': 'دسترسی جزییات کلاس ها'},
        {'name': 'تغییر وضعیت کلاس', 'code': 'class_change_status', 'description': 'دسترسی تغییر وضعیت کلاس ها'},
    ]
}
PERMISSIONS.append(CLASS_PERMISSIONS)

######################################################################

COURSE_PERMISSIONS = {
    'title': 'دسترسی دوره ها',
    'permissions': [
        {'name': 'لیست دوره ها', 'code': 'course_list', 'description': 'دسترسی لیست دوره ها'},
        {'name': 'افزودن دوره', 'code': 'course_create', 'description': 'دسترسی ساخت دوره جدید'},
        {'name': 'ویرایش دوره', 'code': 'course_edit', 'description': 'دسترسی ویرایش دوره ها'},
        {'name': 'حذف دوره', 'code': 'course_delete', 'description': 'دسترسی حذف دوره ها'},
        {'name': 'جزییات دوره', 'code': 'course_detail', 'description': 'دسترسی جزییات دوره ها'},
        {'name': 'تغییر وضعیت دوره', 'code': 'course_change_status', 'description': 'دسترسی تغییر وضعیت دوره ها'},
    ]
}
PERMISSIONS.append(COURSE_PERMISSIONS)

######################################################################

STUDENT_PERMISSIONS = {
    'title': 'دسترسی هنرجو ها',
    'permissions': [
        {'name': 'لیست هنرجو ها', 'code': 'student_list', 'description': 'دسترسی لیست هنرجو ها'},
        {'name': 'افزودن هنرجو', 'code': 'student_create', 'description': 'دسترسی ساخت هنرجو جدید'},
        {'name': 'ویرایش هنرجو', 'code': 'student_edit', 'description': 'دسترسی ویرایش هنرجو ها'},
        {'name': 'حذف هنرجو', 'code': 'student_delete', 'description': 'دسترسی حذف هنرجو ها'},
        {'name': 'جزییات هنرجو', 'code': 'student_detail', 'description': 'دسترسی جزییات هنرجو ها'},
        {'name': 'تغییر وضعیت هنرجو', 'code': 'student_change_status', 'description': 'دسترسی تغییر وضعیت هنرجو ها'},
    ]
}
PERMISSIONS.append(STUDENT_PERMISSIONS)

######################################################################

TEACHER_PERMISSIONS = {
    'title': 'دسترسی مدرس ها',
    'permissions': [
        {'name': 'لیست مدرس ها', 'code': 'teacher_list', 'description': 'دسترسی لیست مدرس ها'},
        {'name': 'افزودن مدرس', 'code': 'teacher_create', 'description': 'دسترسی ساخت مدرس جدید'},
        {'name': 'ویرایش مدرس', 'code': 'teacher_edit', 'description': 'دسترسی ویرایش مدرس ها'},
        {'name': 'حذف مدرس', 'code': 'teacher_delete', 'description': 'دسترسی حذف مدرس ها'},
        {'name': 'جزییات مدرس', 'code': 'teacher_detail', 'description': 'دسترسی جزییات مدرس ها'},
        {'name': 'تغییر وضعیت مدرس', 'code': 'teacher_change_status', 'description': 'دسترسی تغییر وضعیت مدرس ها'},
    ]
}
PERMISSIONS.append(TEACHER_PERMISSIONS)

######################################################################

COURSE_USER_PERMISSIONS = {
    'title': 'دسترسی دوره کاربران',
    'permissions': [
        {'name': 'لیست دوره کاربران', 'code': 'course_user_list', 'description': 'دسترسی لیست دوره کاربران'},
        {'name': 'افزودن دوره کاربران', 'code': 'course_user_create', 'description': 'دسترسی ساخت دوره کاربران جدید'},
        {'name': 'ویرایش دوره کاربران', 'code': 'course_user_edit', 'description': 'دسترسی ویرایش دوره کاربران'},
        {'name': 'حذف دوره کاربران', 'code': 'course_user_delete', 'description': 'دسترسی حذف دوره کاربران'},
        {'name': 'تغییر وضعیت دوره کاربران', 'code': 'course_user_change_status',
         'description': 'دسترسی تغییر وضعیت دوره کاربران'},
    ]
}
PERMISSIONS.append(COURSE_USER_PERMISSIONS)

######################################################################

CLASS_USER_PERMISSIONS = {
    'title': 'دسترسی کاربران کلاس ها',
    'permissions': [
        {'name': 'لیست کاربران کلاس ها', 'code': 'class_user_list', 'description': 'دسترسی لیست کاربران کلاس ها'},
        {'name': 'افزودن کاربران کلاس ها', 'code': 'class_user_create',
         'description': 'دسترسی ساخت کاربران کلاس ها جدید'},
        {'name': 'ویرایش کاربران کلاس ها', 'code': 'class_user_edit', 'description': 'دسترسی ویرایش کاربران کلاس ها'},
        {'name': 'حذف کاربران کلاس ها', 'code': 'class_user_delete', 'description': 'دسترسی حذف کاربران کلاس ها'},
        {'name': 'جزییات(پرداخت شهریه) کاربران کلاس ها', 'code': 'class_user_detail',
         'description': 'دسترسی جزییات(پرداخت شهریه) کلاس ها'},
        {'name': 'تغییر وضعیت کاربران کلاس ها', 'code': 'class_user_change_status',
         'description': 'دسترسی تغییر وضعیت کاربران کلاس ها'},
    ]
}
PERMISSIONS.append(CLASS_USER_PERMISSIONS)

######################################################################

SETTINGS_PERMISSIONS = {
    'title': 'دسترسی تنظیمات',
    'permissions': [
        {'name': 'لیست تنظیمات', 'code': 'setting_list', 'description': 'دسترسی لیست تنظیمات'},
        {'name': 'افزودن تنظیمات', 'code': 'setting_create',
         'description': 'دسترسی ساخت تنظیمات جدید'},
        {'name': 'ویرایش تنظیمات', 'code': 'setting_edit', 'description': 'دسترسی ویرایش تنظیمات'},
        {'name': 'حذف تنظیمات', 'code': 'setting_delete', 'description': 'دسترسی حذف تنظیمات'},
    ]
}
PERMISSIONS.append(SETTINGS_PERMISSIONS)

######################################################################

SLIDERS_PERMISSIONS = {
    'title': 'دسترسی اسلایدر',
    'permissions': [
        {'name': 'لیست اسلایدر', 'code': 'slider_list', 'description': 'دسترسی لیست اسلایدر'},
        {'name': 'افزودن اسلایدر', 'code': 'slider_create',
         'description': 'دسترسی ساخت اسلایدر جدید'},
        {'name': 'ویرایش اسلایدر', 'code': 'slider_edit', 'description': 'دسترسی ویرایش اسلایدر'},
        {'name': 'حذف اسلایدر', 'code': 'slider_delete', 'description': 'دسترسی حذف اسلایدر'},
    ]
}
PERMISSIONS.append(SLIDERS_PERMISSIONS)

######################################################################

CLASS_ATTENDANCE_PERMISSIONS = {
    'title': 'دسترسی حضور و غیاب',
    'permissions': [
        {'name': 'لیست حضور و غیاب', 'code': 'class_attendance_list', 'description': 'دسترسی لیست حضور و غیاب'},
        {'name': 'لیست حضور و غیاب روزانه', 'code': 'class_daily_attendance_list', 'description': 'دسترسی لیست حضور و غیاب روزانه'},
        {'name': 'افزودن حضور و غیاب', 'code': 'class_attendance_create',
         'description': 'دسترسی ساخت حضور و غیاب جدید'},
        {'name': 'ویرایش حضور و غیاب', 'code': 'class_attendance_edit', 'description': 'دسترسی ویرایش حضور و غیاب'},
        {'name': 'حذف حضور و غیاب', 'code': 'class_attendance_delete', 'description': 'دسترسی حذف حضور و غیاب'},
    ]
}
PERMISSIONS.append(CLASS_ATTENDANCE_PERMISSIONS)

######################################################################

CHATS_PERMISSIONS = {
    'title': 'دسترسی پیام',
    'permissions': [
        {'name': 'لیست پیام', 'code': 'chats_list', 'description': 'دسترسی لیست پیام'},
        {'name': 'افزودن پیام', 'code': 'chats_create',
         'description': 'دسترسی ساخت پیام جدید'},
        {'name': 'ویرایش پیام', 'code': 'chats_edit', 'description': 'دسترسی ویرایش پیام'},
        {'name': 'حذف پیام', 'code': 'chats_delete', 'description': 'دسترسی حذف پیام'},
    ]
}
PERMISSIONS.append(CHATS_PERMISSIONS)

######################################################################

REPORT_CARD_PERMISSIONS = {
    'title': 'دسترسی کارنامه',
    'permissions': [
        {'name': 'لیست کارنامه', 'code': 'report_card_list', 'description': 'دسترسی لیست کارنامه'},
        {'name': 'افزودن کارنامه', 'code': 'report_card_create',
         'description': 'دسترسی ساخت کارنامه جدید'},
        {'name': 'ویرایش کارنامه', 'code': 'report_card_edit', 'description': 'دسترسی ویرایش کارنامه'},
        {'name': 'حذف کارنامه', 'code': 'report_card_delete', 'description': 'دسترسی حذف کارنامه'},
    ]
}
PERMISSIONS.append(REPORT_CARD_PERMISSIONS)

######################################################################

BLOG_PERMISSIONS = {
    'title': 'دسترسی مقاله',
    'permissions': [
        {'name': 'لیست مقاله', 'code': 'blog_list', 'description': 'دسترسی لیست مقاله'},
        {'name': 'افزودن مقاله', 'code': 'blog_create',
         'description': 'دسترسی ساخت مقاله جدید'},
        {'name': 'ویرایش مقاله', 'code': 'blog_edit', 'description': 'دسترسی ویرایش مقاله'},
        {'name': 'حذف مقاله', 'code': 'blog_delete', 'description': 'دسترسی حذف مقاله'},
    ]
}
PERMISSIONS.append(BLOG_PERMISSIONS)

######################################################################

BLOG_CATEGORY_PERMISSIONS = {
    'title': 'دسترسی دسته بندی مقاله',
    'permissions': [
        {'name': 'لیست دسته بندی مقاله', 'code': 'blog_category_list', 'description': 'دسترسی لیست دسته بندی مقاله'},
        {'name': 'افزودن دسته بندی مقاله', 'code': 'blog_category_create',
         'description': 'دسترسی ساخت دسته بندی مقاله جدید'},
        {'name': 'ویرایش دسته بندی مقاله', 'code': 'blog_category_edit',
         'description': 'دسترسی ویرایش دسته بندی مقاله'},
        {'name': 'حذف دسته بندی مقاله', 'code': 'blog_category_delete', 'description': 'دسترسی حذف دسته بندی مقاله'},
    ]
}
PERMISSIONS.append(BLOG_CATEGORY_PERMISSIONS)

######################################################################

CATEGORY_PERMISSIONS = {
    'title': 'دسترسی دسته بندی محصول',
    'permissions': [
        {'name': 'لیست دسته بندی محصول', 'code': 'category_list', 'description': 'دسترسی لیست دسته بندی محصول'},
        {'name': 'افزودن دسته بندی محصول', 'code': 'category_create',
         'description': 'دسترسی ساخت دسته بندی محصول جدید'},
        {'name': 'ویرایش دسته بندی محصول', 'code': 'category_edit', 'description': 'دسترسی ویرایش دسته بندی محصول'},
        {'name': 'حذف دسته بندی محصول', 'code': 'category_delete', 'description': 'دسترسی حذف دسته بندی محصول'},
    ]
}
PERMISSIONS.append(CATEGORY_PERMISSIONS)

######################################################################

PRODUCT_PERMISSIONS = {
    'title': 'دسترسی محصول',
    'permissions': [
        {'name': 'لیست محصول', 'code': 'product_list', 'description': 'دسترسی لیست محصول'},
        {'name': 'افزودن محصول', 'code': 'product_create',
         'description': 'دسترسی ساخت محصول جدید'},
        {'name': 'ویرایش محصول', 'code': 'product_edit', 'description': 'دسترسی ویرایش محصول'},
        {'name': 'حذف محصول', 'code': 'product_delete', 'description': 'دسترسی حذف محصول'},
    ]
}
PERMISSIONS.append(PRODUCT_PERMISSIONS)

######################################################################

USER_PRODUCT_PERMISSIONS = {
    'title': 'دسترسی محصولات کاربران',
    'permissions': [
        {'name': 'لیست محصولات کاربران', 'code': 'user_product_list', 'description': 'دسترسی لیست محصولات کاربران'},
        {'name': 'حذف محصولات کاربران', 'code': 'user_product_delete', 'description': 'دسترسی حذف محصولات کاربران'},
    ]
}
PERMISSIONS.append(USER_PRODUCT_PERMISSIONS)

######################################################################

TICKET_PERMISSIONS = {
    'title': 'دسترسی تیکت',
    'permissions': [
        {'name': 'لیست تیکت', 'code': 'ticket_list', 'description': 'دسترسی لیست تیکت'},
        {'name': 'افزودن تیکت', 'code': 'ticket_create',
         'description': 'دسترسی ساخت تیکت جدید'},
        {'name': 'ویرایش تیکت', 'code': 'ticket_edit', 'description': 'دسترسی ویرایش تیکت'},
        {'name': 'حذف تیکت', 'code': 'ticket_delete', 'description': 'دسترسی حذف تیکت'},
    ]
}
PERMISSIONS.append(TICKET_PERMISSIONS)

######################################################################

TICKET_ANSWER_PERMISSIONS = {
    'title': 'دسترسی پاسخ تیکت ها',
    'permissions': [
        {'name': 'لیست پاسخ تیکت ها', 'code': 'ticket_answer_list', 'description': 'دسترسی لیست پاسخ تیکت ها'},
        {'name': 'افزودن پاسخ تیکت ها', 'code': 'ticket_answer_create',
         'description': 'دسترسی ساخت پاسخ تیکت ها جدید'},
        {'name': 'ویرایش پاسخ تیکت ها', 'code': 'ticket_answer_edit', 'description': 'دسترسی ویرایش پاسخ تیکت ها'},
        {'name': 'حذف پاسخ تیکت ها', 'code': 'ticket_answer_delete', 'description': 'دسترسی حذف پاسخ تیکت ها'},
    ]
}
PERMISSIONS.append(TICKET_ANSWER_PERMISSIONS)

######################################################################

HELPS_PERMISSIONS = {
    'title': 'دسترسی متون راهنما',
    'permissions': [
        {'name': 'لیست متون راهنما', 'code': 'helps_answer_list', 'description': 'دسترسی لیست متون راهنما'},
        {'name': 'افزودن متون راهنما', 'code': 'helps_answer_create',
         'description': 'دسترسی ساخت متون راهنما جدید'},
        {'name': 'ویرایش متون راهنما', 'code': 'helps_answer_edit', 'description': 'دسترسی ویرایش متون راهنما'},
        {'name': 'حذف متون راهنما', 'code': 'helps_answer_delete', 'description': 'دسترسی حذف متون راهنما'},
    ]
}
PERMISSIONS.append(HELPS_PERMISSIONS)

######################################################################

SUGGESTION_PERMISSIONS = {
    'title': 'دسترسی انتقادات و پیشنهادات ها',
    'permissions': [
        {'name': 'لیست انتقادات و پیشنهادات ها', 'code': 'suggestion_list',
         'description': 'دسترسی لیست انتقادات و پیشنهادات ها'},
        {'name': 'افزودن انتقادات و پیشنهادات ها', 'code': 'suggestion_create',
         'description': 'دسترسی ساخت انتقادات و پیشنهادات ها جدید'},
        {'name': 'ویرایش انتقادات و پیشنهادات ها', 'code': 'suggestion_edit',
         'description': 'دسترسی ویرایش انتقادات و پیشنهادات ها'},
        {'name': 'حذف انتقادات و پیشنهادات ها', 'code': 'suggestion_delete',
         'description': 'دسترسی حذف انتقادات و پیشنهادات ها'},
    ]
}
PERMISSIONS.append(SUGGESTION_PERMISSIONS)

######################################################################

CONTACT_US_PERMISSIONS = {
    'title': 'دسترسی ارتباط باما',
    'permissions': [
        {'name': 'لیست ارتباط باما', 'code': 'contact_us_list', 'description': 'دسترسی لیست ارتباط باما'},
        {'name': 'افزودن ارتباط باما', 'code': 'contact_us_create',
         'description': 'دسترسی ساخت ارتباط باما جدید'},
        {'name': 'ویرایش ارتباط باما', 'code': 'contact_us_edit', 'description': 'دسترسی ویرایش ارتباط باما'},
        {'name': 'حذف ارتباط باما', 'code': 'contact_us_delete', 'description': 'دسترسی حذف ارتباط باما'},
    ]
}
PERMISSIONS.append(CONTACT_US_PERMISSIONS)

######################################################################

PRODUCT_USER_PERMISSIONS = {
    'title': 'دسترسی نمایش محصولات به کاربران ها',
    'permissions': [
        {'name': 'لیست نمایش محصولات به کاربران ها', 'code': 'product_user_list',
         'description': 'دسترسی لیست نمایش محصولات به کاربران ها'},
        {'name': 'جزییات نمایش محصولات به کاربران ها', 'code': 'product_user_detail',
         'description': 'دسترسی جزییات نمایش محصولات به کاربران ها جدید'},
    ]
}
PERMISSIONS.append(PRODUCT_USER_PERMISSIONS)

######################################################################

QUIZ_PERMISSIONS = {
    'title': 'دسترسی آزمون ها',
    'permissions': [
        {'name': 'لیست آزمون ها', 'code': 'quiz_list', 'description': 'دسترسی لیست آزمون ها'},
        {'name': 'افزودن آزمون ها', 'code': 'quiz_create',
         'description': 'دسترسی ساخت آزمون ها جدید'},
        {'name': 'ویرایش آزمون ها', 'code': 'quiz_edit', 'description': 'دسترسی ویرایش آزمون ها'},
        {'name': 'حذف آزمون ها', 'code': 'quiz_delete', 'description': 'دسترسی حذف آزمون ها'},
        {'name': 'جزییات آزمون ها', 'code': 'quiz_detail', 'description': 'دسترسی جزییات آزمون ها'},
        {'name': 'تغییر وضعیت آزمون ها', 'code': 'quiz_change_status',
         'description': 'دسترسی تغییر وضعیت آزمون ها'},
    ]
}
PERMISSIONS.append(QUIZ_PERMISSIONS)

######################################################################

USER_QUIZ_PERMISSIONS = {
    'title': 'دسترسی پاسخنامه ها',
    'permissions': [
        {'name': 'لیست پاسخنامه ها', 'code': 'user_quiz_list', 'description': 'دسترسی لیست پاسخنامه ها'},
        {'name': 'افزودن پاسخنامه ها', 'code': 'user_quiz_create',
         'description': 'دسترسی ساخت پاسخنامه ها جدید'},
        {'name': 'ویرایش پاسخنامه ها', 'code': 'user_quiz_edit', 'description': 'دسترسی ویرایش پاسخنامه ها'},
        {'name': 'حذف پاسخنامه ها', 'code': 'user_quiz_delete', 'description': 'دسترسی حذف پاسخنامه ها'},
        {'name': 'جزییات پاسخنامه ها', 'code': 'user_quiz_detail', 'description': 'دسترسی جزییات پاسخنامه ها'},
        {'name': 'ثبت نمره پاسخنامه ها', 'code': 'user_quiz_score', 'description': 'دسترسی ثبت نمره پاسخنامه ها'},
        {'name': 'تغییر وضعیت پاسخنامه ها', 'code': 'user_quiz_change_status',
         'description': 'دسترسی تغییر وضعیت پاسخنامه ها'},
    ]
}
PERMISSIONS.append(USER_QUIZ_PERMISSIONS)

######################################################################

INSTALLMENT_PERMISSIONS = {
    'title': 'دسترسی قسط شهریه ها',
    'permissions': [
        {'name': 'لیست قسط شهریه ها', 'code': 'installment_list', 'description': 'دسترسی لیست قسط شهریه ها'},
        {'name': 'افزودن قسط شهریه ها', 'code': 'installment_create',
         'description': 'دسترسی ساخت قسط شهریه ها جدید'},
        {'name': 'ویرایش قسط شهریه ها', 'code': 'installment_edit', 'description': 'دسترسی ویرایش قسط شهریه ها'},
        {'name': 'حذف قسط شهریه ها', 'code': 'installment_delete', 'description': 'دسترسی حذف قسط شهریه ها'},
        {'name': 'جزییات قسط شهریه ها', 'code': 'installment_detail', 'description': 'دسترسی جزییات قسط شهریه ها'},
    ]
}
PERMISSIONS.append(INSTALLMENT_PERMISSIONS)

######################################################################

INSTALLMENT_PAYMENTS_PERMISSIONS = {
    'title': 'دسترسی تقسیم های قسط شهریه ها',
    'permissions': [
        {'name': 'لیست تقسیم های قسط شهریه ها', 'code': 'installment_items_list',
         'description': 'دسترسی لیست تقسیم های قسط شهریه ها'},
        {'name': 'افزودن تقسیم های قسط شهریه ها', 'code': 'installment_items_create',
         'description': 'دسترسی ساخت تقسیم های قسط شهریه ها جدید'},
        {'name': 'ویرایش تقسیم های قسط شهریه ها', 'code': 'installment_items_edit',
         'description': 'دسترسی ویرایش تقسیم های قسط شهریه ها'},
        {'name': 'حذف تقسیم های قسط شهریه ها', 'code': 'installment_items_delete',
         'description': 'دسترسی حذف تقسیم های قسط شهریه ها'},
        {'name': 'جزییات های تقسیم قسط شهریه ها', 'code': 'installment_items_detail',
         'description': 'دسترسی جزییات تقسیم های قسط شهریه ها'},
    ]
}
PERMISSIONS.append(INSTALLMENT_PAYMENTS_PERMISSIONS)

######################################################################

SMS_PERMISSIONS = {
    'title': 'دسترسی پیامک ها',
    'permissions': [
        {'name': 'لیست پیامک ها', 'code': 'sms_list', 'description': 'دسترسی لیست تراکنش ها'},
        {'name': 'ارسال پیامک ها', 'code': 'sms_send', 'description': 'دسترسی ارسال تراکنش ها'},
    ]
}
PERMISSIONS.append(SMS_PERMISSIONS)

######################################################################

PAYMENTS_PERMISSIONS = {
    'title': 'دسترسی تراکنش ها',
    'permissions': [
        {'name': 'لیست تراکنش ها', 'code': 'payments_list', 'description': 'دسترسی لیست تراکنش ها'},
    ]
}
PERMISSIONS.append(PAYMENTS_PERMISSIONS)

######################################################################

BLO_COMMENTS_PERMISSIONS = {
    'title': 'دسترسی نظرات',
    'permissions': [
        {'name': 'لیست نظرات', 'code': 'blog_comments_list', 'description': 'دسترسی لیست نظرات'},
        {'name': 'تغییر وضعیت نظرات', 'code': 'blog_comments_change_status', 'description': 'دسترسی تغییر وضعیت نظرات'},
        {'name': 'حذف نظرات', 'code': 'blog_comments_delete', 'description': 'دسترسی حذف نظرات'},
    ]
}
PERMISSIONS.append(BLO_COMMENTS_PERMISSIONS)

######################################################################

POLL_PERMISSIONS = {
    'title': 'دسترسی فرم نظرسنجی ها',
    'permissions': [
        {'name': 'لیست فرم نظرسنجی ها', 'code': 'poll_list', 'description': 'دسترسی لیست فرم نظرسنجی ها'},
        {'name': 'افزودن فرم نظرسنجی', 'code': 'poll_create', 'description': 'دسترسی ساخت فرم نظرسنجی جدید'},
        {'name': 'ویرایش فرم نظرسنجی', 'code': 'poll_edit', 'description': 'دسترسی ویرایش فرم نظرسنجی ها'},
        {'name': 'حذف فرم نظرسنجی', 'code': 'poll_delete', 'description': 'دسترسی حذف فرم نظرسنجی ها'},
        {'name': 'جزییات فرم نظرسنجی', 'code': 'poll_detail', 'description': 'دسترسی جزییات فرم نظرسنجی ها'},
        {'name': 'تغییر وضعیت فرم نظرسنجی', 'code': 'poll_change_status',
         'description': 'دسترسی تغییر وضعیت فرم نظرسنجی ها'},
    ]
}
PERMISSIONS.append(POLL_PERMISSIONS)

######################################################################

CLASS_CATEGORY_PERMISSIONS = {
    'title': 'دسترسی دسته بندی کلاس ها',
    'permissions': [
        {'name': 'لیست دسته بندی کلاس ها', 'code': 'classes_categories_list', 'description': 'دسترسی لیست دسته بندی کلاس ها'},
        {'name': 'افزودن دسته بندی کلاس', 'code': 'classes_categories_create', 'description': 'دسترسی ساخت دسته بندی کلاس جدید'},
        {'name': 'ویرایش دسته بندی کلاس', 'code': 'classes_categories_edit', 'description': 'دسترسی ویرایش دسته بندی کلاس ها'},
        {'name': 'حذف دسته بندی کلاس', 'code': 'classes_categories_delete', 'description': 'دسترسی حذف دسته بندی کلاس ها'}
    ]
}
PERMISSIONS.append(CLASS_CATEGORY_PERMISSIONS)

######################################################################

TEACHER_ATTENDANCE_PERMISSIONS = {
    'title': 'دسترسی حضور و غیاب مدرس ها',
    'permissions': [
        {'name': 'لیست حضور و غیاب مدرس ها', 'code': 'teacher_attendance_list',
         'description': 'دسترسی لیست حضور و غیاب مدرس ها'},
        {'name': 'افزودن حضور و غیاب مدرس', 'code': 'teacher_attendance_create',
         'description': 'دسترسی ساخت حضور و غیاب مدرس جدید'},
        {'name': 'ویرایش حضور و غیاب مدرس', 'code': 'teacher_attendance_edit',
         'description': 'دسترسی ویرایش حضور و غیاب مدرس ها'},
        {'name': 'حذف حضور و غیاب مدرس', 'code': 'teacher_attendance_delete',
         'description': 'دسترسی حذف حضور و غیاب مدرس ها'},
        {'name': 'جزییات حضور و غیاب مدرس', 'code': 'teacher_attendance_detail',
         'description': 'دسترسی جزییات حضور و غیاب مدرس ها'},
        {'name': 'تغییر وضعیت حضور و غیاب مدرس', 'code': 'teacher_attendance_change_status',
         'description': 'دسترسی تغییر وضعیت حضور و غیاب مدرس ها'},
    ]
}
PERMISSIONS.append(TEACHER_ATTENDANCE_PERMISSIONS)

######################################################################

TEACHER_PAYMENTS_PERMISSIONS = {
    'title': 'دسترسی پرداختی مدرس ها',
    'permissions': [
        {'name': 'لیست پرداختی مدرس ها', 'code': 'teacher_payments_list', 'description': 'دسترسی لیست پرداختی مدرس ها'},
        {'name': 'افزودن پرداختی مدرس', 'code': 'teacher_payments_create',
         'description': 'دسترسی ساخت پرداختی مدرس جدید'},
        {'name': 'ویرایش پرداختی مدرس', 'code': 'teacher_payments_edit',
         'description': 'دسترسی ویرایش پرداختی مدرس ها'},
        {'name': 'حذف پرداختی مدرس', 'code': 'teacher_payments_delete', 'description': 'دسترسی حذف پرداختی مدرس ها'},
        {'name': 'جزییات پرداختی مدرس', 'code': 'teacher_payments_detail',
         'description': 'دسترسی جزییات پرداختی مدرس ها'},
        {'name': 'تغییر وضعیت پرداختی مدرس', 'code': 'teacher_payments_change_status',
         'description': 'دسترسی تغییر وضعیت پرداختی مدرس ها'},
    ]
}
PERMISSIONS.append(TEACHER_PAYMENTS_PERMISSIONS)


class ROLE_CODES:
    STUDENT = "student"
    TEACHER = "teacher"
