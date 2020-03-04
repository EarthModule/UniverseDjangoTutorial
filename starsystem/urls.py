from django.urls import path, include
from rest_framework.routers import DefaultRouter
from starsystem import views

router = DefaultRouter()
router.register(r'planets', views.PlanetViewSet, basename='Planets' )
router.register(r'stars', views.StarViewSet, basename='Stars')
router.register(r'reds', views.RedPlanetViewSet, basename='Red Planets')

urlpatterns = [
    path('', include(router.urls))
]