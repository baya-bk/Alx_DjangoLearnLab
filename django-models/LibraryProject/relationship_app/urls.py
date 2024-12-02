from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view

app_name = 'relationship_app'

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('books/', list_books, name='book_list'),  # Example protected view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin/', admin_view, name='admin_view'),  # Admin view URL
    path('librarian/', librarian_view,
         name='librarian_view'),  # Librarian view URL
    path('member/', member_view, name='member_view'),  # Member view URL
]
