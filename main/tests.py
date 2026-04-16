from django.test import Client, TestCase


class ExtendedStatusCodeTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_request_preserves_status_code_above_599(self):
        response = self.client.get('/', {'status': '600'})

        self.assertEqual(response.status_code, 600)

    def test_post_request_preserves_status_code_above_599(self):
        response = self.client.post('/', {'status': '600'})

        self.assertEqual(response.status_code, 600)
