from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book, Author

# Create your views here.
def homepage(req):
    return HttpResponse("<h1>Hello! Here are all the books!<h1>")
    data = { 'books': Book.objects.all() }
    return render(request, 'books/home.html', data)


def not_found_404(request, exception):
    data = { 'err': exception}
    return render(request, 'adoption/404.html', data)

# def home(request):
#     data = { 'books': Book.objects.all() }
#     return render(request, 'books/home.html', data)

def show(req, book_id):
    # data = { 'books' : Book.objects.get(pk={book_id})}
    # return HttpResponse(f'<h3>Book number {book_id}</h3>')
    if Book.objects.filter(id=book_id).exists():
        book = get_object_or_404(Book, pk=book_id)

        data = {
            'book' : book
        }
        # return HttpResponse(
        #     Book.objects.get(id=book_id).title,
        #     Book.objects.get(id=book_id).author
        # )
        return render(req, 'books/book_by_id.html', data)
    else:
        return HttpResponse("We do not have a book with that ID")
    




# def specific_joke(request, joke_id):
# if Joke.objects.filter(id=joke_id).exists():
#     return HttpResponse(
#         Joke.objects.get(id=joke_id).text
#     )
# else:
#     return HttpResponse("Sorry, no joke with that ID exists")
