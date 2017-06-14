from django.conf.urls import include, url
from django.contrib import admin
import search.views as sv
urlpatterns = [
    # Examples:
    # url(r'^$', 'es.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', sv.car_search),
]
