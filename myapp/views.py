from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    # context = {
    #     "hello" : "hello rachana"
    # }
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")   

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        details = request.POST.get("details")
        phone = request.POST.get("phone")
        contact = Contact(name=name, email = email, details=details,phone=phone,date=datetime.today())
        contact.save()
    return render(request, "contact.html")      