from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.base import RedirectView

from apps.shortener.forms import ShortUrlForm
from apps.shortener.models import ShortUrl
from conf.settings import DEFAULT_PAGINATION


class IndexView(CreateView):
    model = ShortUrl
    form_class = ShortUrlForm
    template_name = "shortener/index.html"
    success_url = reverse_lazy("shortener:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        short_urls = ShortUrl.objects.order_by("-created_at")
        paginator = Paginator(short_urls, DEFAULT_PAGINATION)
        context['page_obj'] = paginator.get_page(self.request.GET.get("page"))
        return context

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
