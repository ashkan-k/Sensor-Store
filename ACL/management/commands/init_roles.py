from django.core.management import BaseCommand
from ACL.models import *
from ACL.permissions import PERMISSIONS, ROLE_CODES

STUDENT_PERMS = [
    'class_list',
    'class_detail',
    'course_list',
    'course_detail',

    'teacher_detail',

    'chats_list',
    'chats_create',
    'chats_edit',
    'chats_delete',

    'report_card_list',

    'ticket_list',
    'ticket_create',
    'ticket_edit',
    'ticket_delete',

    'ticket_answer_list',
    'ticket_answer_create',
    'ticket_answer_edit',
    'ticket_answer_delete',

    'suggestion_list',
    'suggestion_create',
    'suggestion_edit',
    'suggestion_delete',

    'class_detail',

    'product_user_list',
    'product_user_detail',

    'quiz_list',
    'quiz_detail',

    'payments_list',

    'class_user_detail',

    'user_quiz_list',
    'user_quiz_detail',

    'installment_list',
    'installment_detail',
    'installment_items_list',
    'installment_items_detail',

    'poll_list',
]

TEACHER_PERMS = [
    'course_user_list',

    'class_user_list',

    'class_attendance_list',
    'class_attendance_create',
    'class_attendance_edit',
    'class_attendance_delete',

    'student_detail',

    'class_list',
    'class_detail',
    'course_list',
    'course_detail',

    'chats_list',
    'chats_create',
    'chats_edit',
    'chats_delete',

    'suggestion_list',
    'suggestion_create',
    'suggestion_edit',
    'suggestion_delete',

    'product_user_list',
    'product_user_detail',

    'quiz_list',
    'quiz_detail',

    'payments_list',

    'user_quiz_list',
    'user_quiz_detail',
    'user_quiz_score',
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='clear old states and cities',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Role.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"CLEAR"))

        role, created = Role.objects.update_or_create(name='هنرجو', code=ROLE_CODES.STUDENT)
        role.permissions.set(Permission.objects.filter(code__in=STUDENT_PERMS))

        ##############################################################################################

        role, created = Role.objects.update_or_create(name='مدرس', code=ROLE_CODES.TEACHER)
        role.permissions.set(Permission.objects.filter(code__in=TEACHER_PERMS))
        self.stdout.write(self.style.SUCCESS(f"DONE..."))
