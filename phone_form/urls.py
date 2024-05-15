from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "phone_form"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("api/get-phone-number-info/", views.get_phone_number_info, name="get_phone_number_info")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)