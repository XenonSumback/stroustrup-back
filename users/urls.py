from django.conf.urls import url

from users import views


urlpatterns = [
    url(r'^login/$', views.user_auth),
    url(r'^registration/$', views.registration),
    url(r'^logout/$', views.logout_view),
    url(r'^whoami/', views.whoami_view)
]
