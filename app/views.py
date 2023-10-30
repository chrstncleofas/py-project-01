from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'interface/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # I-redirect ang user sa homepage
    else:
        form = UserCreationForm()
    return render(request, 'interface/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # I-redirect ang user sa homepage
    else:
        form = AuthenticationForm()
    return render(request, 'interface/login.html', {'form': form})
