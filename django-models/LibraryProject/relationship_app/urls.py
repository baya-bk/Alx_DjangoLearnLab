from django.contrib.auth import views as auth_views
from .views import register, logout_view
from django.urls import path
from .views import list_books
from .views import LibraryDetailView


app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:login'), name='logout'),
    path('register/', register, name='register'),
    path('logout_page/', logout_view, name='logout_page'),
]
