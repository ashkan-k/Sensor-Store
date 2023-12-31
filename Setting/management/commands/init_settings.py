import os
from django.core.management import BaseCommand
from ACL.models import *
from Setting.models import Setting
from config.settings import STATIC_URL

DEFAULT_SETTINGS = {
    # info
    'vision_about': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.""",
    'about_us': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.""",
    'contact_us': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.""",
    'terms_text': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.""",
    'copyright': """کپی رایت ©2022""",
    'logo': """/static/front/img/logo.png""",
    'address': """تهران کوچه اول پلاک دوم طبقه سوم واحد چهارم""",
    'tel': """+98 21 6656 6656""",
    'footer_about_us': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است""",
    'today_join_us_text': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است.""",
    'courses_intro_text': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد""",
    'courses_intro_text_lists': """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد""",

    # Social
    'email': """yourmail@Saei.com""",
    'telegram': """saei""",
    'whatsapp': """https://wa.me/qr/L7BFPCZNPX7QB1""",
    'twitter': """saei""",
    'youtube': """saei""",
    'instagram': """saei""",

    # Links
    'home_link': """http://127.0.0.1:8000/""",
    'about_link': """http://127.0.0.1:8000/about/""",
    'class_link': """http://127.0.0.1:8000/courses""",
    'contact_link': """http://127.0.0.1:8000/contact_us/""",
    'reportCard_link': """http://127.0.0.1:8000/report-card/""",
    'teacher_link': """http://127.0.0.1:8000/teachers/""",

    # ContactUs Map
    'map_lat': "10.0",
    'map_long': "10.0",

    # Index Poster
    'poster_image': STATIC_URL + os.path.join('front/images/video.jpg'),
    'poster_video': 'https://youtu.be/5_MRXyYjHDk',

    # Index Poster
    'about_us_image1': STATIC_URL + os.path.join('front/images/about_1.jpg'),
    'about_us_image2': STATIC_URL + os.path.join('front/images/about_1.jpg'),
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='clear old states and cities',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Setting.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"CLEAR"))

        for key, value in DEFAULT_SETTINGS.items():
            obj, _ = Setting.objects.get_or_create(key=key)
            obj.value = value
            obj.save()

        self.stdout.write(self.style.SUCCESS(f"DONE..."))
