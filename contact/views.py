from django.shortcuts import render, redirect
from .models import Contact


def index(request):
    contact_lists = Contact.objects.all()

    return render(request, 'index.html', {'contact_lists': contact_lists})


def create(request):

    if request.method == 'POST':
        full_name = request.POST['fullname']
        relationship = request.POST['relationship']
        phone_number = request.POST['phone-number']
        email = request.POST['email']
        address = request.POST['address']

        data = Contact(full_name=full_name, relationship=relationship,
                       phone_number=phone_number, email=email, address=address)

        data.save()

        return redirect('/')

    return render(request, 'create-contact.html')


def details(request, pk):
    contact = Contact.objects.get(pk=pk)

    return render(request, 'contact-profile.html', {'contact': contact})


def edit(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']

        contact.save()

        return redirect('/')

    return render(request, 'edit.html', {'contact': contact})


def destroy(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contact': contact})


def search(request):

    if request.method == "POST":
        name = request.POST['search-area']
        contact = Contact.objects.filter(full_name__icontains=name)
        return render(request, 'index.html', {'contact_lists': contact, 'name': name})

    return redirect('/')
