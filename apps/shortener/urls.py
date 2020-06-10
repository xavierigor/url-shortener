from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'shortener'


urlpatterns = [

    path("", views.IndexView.as_view(), name="index"),
    path("<short_url_code>", views.AccessUrlRedirectView.as_view(), name="access_url"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
