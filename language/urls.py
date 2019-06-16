from django.urls import path, include
from .views import LanguageView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', LanguageView)

urlpatterns = [
    path('', include(router.urls)),
]