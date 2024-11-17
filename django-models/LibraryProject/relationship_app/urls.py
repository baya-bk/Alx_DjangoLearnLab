from django.contrib.auth import views as auth_views
from .views import login_view
from .views import register_view
from .views import logout_view
from .views import list_books
from django.urls import path
from .views import list_books
from .views import LibraryDetailView


app_name = 'relationship_app'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('books/', list_books, name='book_list'),  # Example protected view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
