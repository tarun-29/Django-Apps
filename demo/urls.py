# from xml.etree.ElementInclude import include
from django.urls import path, include

# from demo.models import Book
# from . import views
from rest_framework import routers
from .views import BookViewSet
# from .views import Another

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('another',Another.as_view()),
]
