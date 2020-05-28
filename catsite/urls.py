from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework import routers

from catapp import views

router = routers.DefaultRouter()
router.register(
    r'api/breed',
    views.BreedViewSet
)
router.register(
    r'api/cat',
    views.CatViewSet
)
router.register(
    r'api/human',
    views.HumanViewSet
)
router.register(
    r'api/home',
    views.HomeViewSet
)

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    path(
        'admin/',
        admin.site.urls
    ),
]
