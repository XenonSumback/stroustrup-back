from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^login/$', views.example_view),
]
