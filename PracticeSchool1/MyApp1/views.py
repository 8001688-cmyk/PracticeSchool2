import http
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime 
from .models import teacher
from .forms import InputForm
from django.contrib.auth.models import User
from .forms import SignUpForm
from pypdf import PdfWriter, PdfReader #Joining PDFs
from reportlab.pdfgen import canvas #Generating PDfs
from .forms import PDFUploadForm #Upload PDF

from reportlab.platypus import Paragraph,Image,Table #Generating PDfs

from django.http import FileResponse #Downloading files

from django.contrib.staticfiles.storage import staticfiles_storage #Working with static files

from io import BytesIO #Using Byte stream


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
            return redirect("home")

    else:
        form = SignUpForm()

    return render(request, "MyApp1/signup.html", {"form": form})

# HomePage

def home(request):
    return render(request, "MyApp1/home.html")        

# PDF

def report(request):
    pdf_file = staticfiles_storage.path("DS.pdf")

    try: 
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="Attachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="noAttachment.pdf")

    return response 

def generate_pdf():
    
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    lines = [('Name', 'Teaching Area:')]

    teachers = teacher.objects.all()

    for teach in teachers: 
        lines.append((teach.Name, teach.Area))
    
    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer 

# Outline Gen

def outline(request):
       return render(request, "MyApp1/outline.html")     

# PDF uploader

def upload_pdf(request):

    if request.method == "POST":
        
        form = PDFUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PDFUploadForm()

    return render(request, "MyApp1/upload_pdf.html", {"form": form})




