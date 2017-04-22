from django.contrib import admin
from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view())
]
