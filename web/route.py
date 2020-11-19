from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/gen', GenViewSet)
router.register(r'api/author', AuthorViewSet)