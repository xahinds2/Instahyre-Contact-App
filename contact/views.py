from faker import Faker
from contact.models import Contact
from django.db.models import Q
from django.shortcuts import render

fake = Faker()


def dashboard(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        Contact.objects.create(name=name, mobile=mobile, email=email)

    context = {
        'contacts': Contact.objects.all().values()
    }

    return render(request, 'dashboard.html', context)


def search_contacts(request):

    if request.method == 'POST':
        query = request.POST.get('query')

        if query:
            contacts = Contact.objects.filter(
                Q(name__icontains=query) | Q(mobile__icontains=query)
            )

            context = {
                'contacts': contacts,
                'query': query
            }

            return render(request, 'search.html', context)

    return render(request, 'search.html')


def populate(request, qty):

    for _ in range(qty):
        name = fake.name()
        mobile = fake.phone_number()
        email = fake.email()
        spam = fake.pybool()
        Contact.objects.create(name=name, mobile=mobile, email=email, spam=spam)

    context = {
        'contacts': Contact.objects.all().values()
    }

    return render(request, 'dashboard.html', context)
