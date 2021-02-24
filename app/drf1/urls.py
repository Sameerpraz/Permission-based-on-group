from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers

from app.drf1.views import *
# from .views import RegisterView

# from .views import MyObtainTokenPairView
# from rest_framework_simplejwt.views import TokenRefreshView
# ViewSets define the view behavior.
# from .views import RegisterView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register('category',CategoryViewSet)
router.register('food',FoodViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]