from utils.tests import MainTestMixin
from User.models import User


class TestAuth(MainTestMixin):
    def test_login(self):
        User.objects.create_user('09115555555', '123')
        data = {
            'phone': '09115555555',
            'password': '123',
        }

        url = '/login'
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 301)
