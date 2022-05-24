from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'journals', views.BookViewSet, basename='journals')

urlpatterns += router.urls