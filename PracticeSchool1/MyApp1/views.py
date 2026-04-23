import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime 
from .models import teacher
from .forms import InputForm
from django.contrib.auth.models import User
from .forms import SignUpForm

# Teachers #

def index(request):

    teach = teacher.objects.all()
    return render(request,"MyApp1/index.html",{'content':teach})

def input_view(request):
    if request.method == "POST":    
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = InputForm()

    return render(request, "MyApp1/input.html", {"form": form})

# delete teachers


def delete_teacher(request, teacher_id):
    t = teacher.objects.get(id=teacher_id)
    t.delete()
    return redirect("index")


# SignUp 

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("index")

    else:
        form = SignUpForm()

    return render(request, "MyApp1/signup.html", {"form": form})
                