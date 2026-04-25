from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.


# create book ----------------

def home(request):
    return render(request, 'home.html')

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= BookForm()

    return render(request, 'book_create.html',{'form' : form})


# read book ----------------



def book_list(request):
    return render(request,'book_list.html', {'books' : Book.objects.all()})

# book detail

def book_detail(request, id):
    # get_object_or_404 prevents the 'None' error we discussed earlier
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_detail.html', {'book': book})

# book update ---------

def book_update(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()

            return redirect("book_list")

    else:

        return render(request, 'book_create.html',{'form': BookForm(instance=book)})
    

# book delete

def book_delete(request, id):
    # 'get_object_or_404' use karein taaki invalid ID par server crash na ho
    book = get_object_or_404(Book, pk=id)
    
    if request.method == 'POST':
        book.delete()
        return redirect("book_list")
    
    # Agar GET request hai (user ne delete button click kiya hai),
    # toh use confirmation page dikhayein.
    return render(request, 'book_confirm_delete.html', {'book': book})