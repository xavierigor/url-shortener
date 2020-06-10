from django.db import models
from .utils import generate_random_string


def unique_short_url():
    url_exists = True

    while url_exists:
        short_url = generate_random_string()
        try:
            ShortUrl.objects.get(short=short_url)
        except ShortUrl.DoesNotExist:
            url_exists = False

    return short_url


class ShortUrl(models.Model):
    full = models.URLField('full url', max_length=500)
    short = models.URLField(unique=True, default=unique_short_url)
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short
