from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # URL for the function-based view
    path('books/', list_books, name='list_books'),
    # URL for the class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(),
         name='library_detail'),
]
