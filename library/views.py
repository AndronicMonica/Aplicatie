from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.views.generic import TemplateView, ListView
from library.models import Book, Imprumuturi

class Index(TemplateView):
    template_name = "base.html"

class BookListView(ListView):
    template_name = "book_list.html"
    queryset = Book.objects.all()

    class Meta:
        default_permissions = ( 'view' )

class ImprumuturiListView(ListView):
    template_name = "imprumuturi_list.html"
    queryset = Imprumuturi.objects.all()
    class Meta:
        default_permissions = ( 'view' )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class imprumutLista:
    def imprumuturiLista():
        return ImprumuturiListView.as_view()