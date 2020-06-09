from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.shortener.forms import ShortUrlForm
from apps.shortener.models import ShortUrl


class IndexView(CreateView):
    model = ShortUrl
    form_class = ShortUrlForm
    template_name = "shortener/index.html"
    success_url = reverse_lazy("shortener:index")

