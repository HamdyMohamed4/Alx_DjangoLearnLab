from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    
    path('books/', BookList.as_view(), name='book-list'),

    
    path('', include(router.urls)),

    path('auth-token/', obtain_auth_token, name='auth-token'),
    path('', include(router.urls)),  # Existing router setup
]












