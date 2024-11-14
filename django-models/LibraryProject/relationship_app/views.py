from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library


def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    # Render the template with book data
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify the template to use

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books related to the library to the context
        context['books'] = self.object.books.all()
        return context
