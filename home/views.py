from django.shortcuts import render
from home.models import Contact  # Import directly from the 'models' module

def contact(request):
    if request.method == "POST":
        # Handle the POST request logic here
        name = request.POST['name']
        desc = request.POST['desc']
        email = request.POST['email']
        print(name,desc,email)
        # Create a new Contact object and save it to the database
        ins = Contact(name=name, email=email, desc=desc)
        ins.save()
        
        print('The data has been written to the db')
        return render(request, 'contact.html')
    elif request.method == "GET":
        return render(request, 'contact.html')
def home(request):
    # Your view logic here
    return render(request, 'home.html')
def about(request):
    # Your view logic here
    return render(request, 'about.html')
def projects(request):
    # Your view logic here
    return render(request, 'projects.html')