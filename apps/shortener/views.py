from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import RedirectView

from apps.shortener.forms import ShortUrlForm
from apps.shortener.models import ShortUrl


class IndexView(CreateView):
    model = ShortUrl
    form_class = ShortUrlForm
    template_name = "shortener/index.html"
    success_url = reverse_lazy("shortener:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urls'] = ShortUrl.objects.order_by("-created_at")
        return context


class AccessUrlRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        short_url = get_object_or_404(ShortUrl, short=kwargs['short'])
        short_url.clicks += 1
        short_url.save()

        self.url = short_url.full

        return super().get_redirect_url(*args, **kwargs)
