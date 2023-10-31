from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
# from geeksforgeeks import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
# from . tokens import generate_token

# Create your views here.
def home(request):
    return render(request, 'interface/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            signin(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'interface/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            signin(request, user)
            # fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            # return render(request, 'authentication/dashboard.html')
            # return render(request, "authentication/dashboard.html",{"fname":fname})
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('dashboard')

    return render(request, 'interface/login.html')

def dashboard(request):
    return render(request, 'interface/dashboard.html')
