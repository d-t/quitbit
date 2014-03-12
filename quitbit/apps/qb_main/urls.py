from django.conf.urls import url, patterns, include
from rest_framework import routers
from views import  UserViewSet, CigaretteViewSet, CommentViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cigarettes', CigaretteViewSet)
router.register(r'comments', CommentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)