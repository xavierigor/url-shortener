from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from apps.shortener.models import ShortUrl


def create_short_url(full_url, short_url=None):
    """
    Create a short url with the given `full_url` and optionally, `short_url`
    """
    if short_url:
        return ShortUrl.objects.create(full=full_url, short=short_url)

    return ShortUrl.objects.create(full=full_url)


class BaseTest(TestCase):
    def setUp(self):
        self.index_url = reverse("shortener:index")
        self.short_url = {"full": "https://testurl.com"}

        return super().setUp()


class IndexTests(BaseTest):

    def test_has_a_short_url_list(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shortener/index.html")
        self.assertTrue("page_obj" in response.context)

    def test_can_shrink_url(self):
        response = self.client.post(self.index_url, self.short_url)
        self.assertEqual(ShortUrl.objects.last().full, "https://testurl.com")
        self.assertEqual(response.status_code, 302)

    def test_invalid_full_url(self):
        url_with_invalid_full_url = create_short_url("invalid-full-url")
        self.assertRaises(ValidationError, url_with_invalid_full_url.full_clean)


class AccessShortUrlTests(BaseTest):

    def test_can_access_short_url(self):
        short_url = create_short_url("https://test-can-access-short-url.com")
        response = self.client.get(short_url.get_absolute_url())
        self.assertEqual(response.status_code, 302)

    def test_invalid_short_url(self):
        url_with_invalid_short_code = reverse("shortener:access_url", kwargs={"short_url_code": "invalid_short_code"})
        response = self.client.get(url_with_invalid_short_code)
        self.assertEqual(response.status_code, 404)
