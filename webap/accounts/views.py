from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Quote
# from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404
from .models import Author

@login_required
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})

@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quote_list.html', {'quotes': quotes})

@login_required
def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'quote_detail.html', {'quote': quote})