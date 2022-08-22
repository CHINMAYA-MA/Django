import email
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .forms import SignUpForm
# Create your views here.
def index(request):
    context = {
        "variable":"this is sent",
    }
    return render(request, 'index.html')
        #return HttpResponse("Welcome to HomePage!!")
def about(request):
        return render(request, 'about.html')
        #return HttpResponse("About")
def forget(request):
        return render(request, 'forget.html')
def services(request):
        return render(request, 'movies.html')
def shows(request):
        return render(request, 'shows.html')
        #return HttpResponse("Services page")
def contact(request):
        if request.method == "POST":
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                desc = request.POST.get('desc')
                contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
                contact.save()
                messages.success(request, 'Profile details updated.')
                def __str__(self):
                        return self.name
        return render(request, 'contact.html')
        #return HttpResponse("contact page")

def loginUser(request):
    if request.method=="POST":
        #check if user has access auth
        username = request.POST.get('username')
        password1 = request.POST.get('password1')  
        user = authenticate(username=username, password1=password1)
        print(username,password1)  
        if user is not None:
            login(request, user)
            print("logged in")
            return redirect("/base")
        else:
            print(" ")
            return render(request, 'index.html')
    return render(request, 'login.html')
 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return render(request, 'login.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})