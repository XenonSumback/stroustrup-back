from django.contrib import admin
from django.conf.urls import url
from users import views
#from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.example_view),
]
