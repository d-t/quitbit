from django.contrib import admin
from django.conf.urls import patterns, include, url


#
# This is the main entry point. All requests passes here and are dispatched to several apps
#

urlpatterns = []

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns += patterns('',

    # include api and main app urls
    url(r'^api/', include('apps.qb_main.urls')),

    # api docs generated
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # comments framework
    (r'^comments/', include('django.contrib.comments.urls')),

    # Admin panel and documentation:
    url(r'^admin/', include(admin.site.urls)),
)
