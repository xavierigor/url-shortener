from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.base import RedirectView

from apps.shortener.forms import ShortUrlForm
from apps.shortener.models import ShortUrl
from conf.settings import DEFAULT_PAGINATION


class IndexView(CreateView, ListView):
    model = ShortUrl
    form_class = ShortUrlForm
    template_name = "shortener/index.html"
    success_url = reverse_lazy("shortener:index")
    paginate_by = DEFAULT_PAGINATION

    def get_queryset(self):
        return ShortUrl.objects.order_by("-created_at")

    def get_success_url(self):
        messages.success(self.request,
                         f"You can access your new URL by <a href='{self.object.get_absolute_url}'>clicking here</a>")
        return super().get_success_url()


class AccessUrlRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        short_url = get_object_or_404(ShortUrl, short=kwargs['short_url_code'])
        short_url.clicks += 1
        short_url.save()

        self.url = short_url.full

        return super().get_redirect_url(*args, **kwargs)
