from django.shortcuts import render

def home(request):
    context = {
        "name": "Sidratul Muntaha",
        "course": "Django Internship",
        "fruits": ["Apple", "Banana", "Mango"]
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "message": "This page demonstrates Django template inheritance."
    }
    return render(request, "about.html", context)