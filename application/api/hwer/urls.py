from . import views

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^recognize/?$', views.RecognizeEquation.as_view(), name="recognize equation"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
