from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


def list_books(request):
    """Function-based view to list all books"""
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class LibraryDetailView(DetailView):
    """Class-based view to display library details"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')


# User Login View

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Change to your desired post-login view
            return redirect('relationship_app:book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View


@login_required
def logout_view(request):
    logout(request)
    return redirect('relationship_app:login')

# User Registration View


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect after successful registration
            return redirect('relationship_app:book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Example of a protected view


@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
