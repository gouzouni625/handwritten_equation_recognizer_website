from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('hwer.urls')),
]
