from django.db import models


class ShortUrl(models.Model):
    full = models.URLField('full url', max_length=500)
    short = models.URLField()
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short
