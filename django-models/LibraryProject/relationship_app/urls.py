from django.contrib.auth import views as auth_views
from .views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books
from django.urls import path
from .views import list_books
from .views import LibraryDetailView


app_name = 'relationship_app'

urlpatterns = [
    path('register/', register, name='register'),  # User registration
    path('books/', list_books, name='book_list'),  # Example protected view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),


    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
