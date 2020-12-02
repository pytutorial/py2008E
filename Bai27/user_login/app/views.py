from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def userView(request): #127.0.0.1:8000/user
    return render(request, 'user.html')

@staff_member_required
def staffView(request): # 127.0.0.1:8000/staff
    return render(request, 'staff.html')

def signup(request):
    form = UserCreationForm()    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, 
                                password=request.POST['password1'])
            login(request, user)
            return redirect('/')    
    context = {'form' : form}
    return render(request, 'registration/signup.html', context)

def index(request):
    return render(request, 'index.html')