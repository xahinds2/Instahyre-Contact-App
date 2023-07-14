from django.contrib.auth.decorators import login_required
from django.db import DataError
from faker import Faker
from contact.models import Contact
from django.db.models import Q
from django.shortcuts import render, redirect

fake = Faker()


@login_required
def my_contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        Contact.objects.create(name=name, mobile=mobile, email=email)

    context = {
        'contacts': Contact.objects.all().values()
    }

    return render(request, 'my_contacts.html', context)


@login_required
def search_contacts(request):

    contacts = []

    if request.method == 'POST':
        query = request.POST.get('query')

        if query:
            contacts += Contact.objects.filter(
                Q(name__startswith=query) | Q(name__contains=query)
            ).order_by('name')

            contacts += Contact.objects.filter(mobile=query)

            context = {
                'contacts': contacts,
                'query': query
            }

            return render(request, 'search_contacts.html', context)

    return render(request, 'search_contacts.html')


@login_required
def spam(request, cid):
    contact = Contact.objects.filter(id=cid).first()
    contact.spam = not contact.spam
    contact.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def populate(request, qty):

    for _ in range(qty):
        name = fake.name()
        mobile = fake.phone_number()
        email = fake.email()
        _spam = fake.pybool()
        try:
            Contact.objects.create(name=name, mobile=mobile, email=email, spam=_spam)
        except DataError:
            pass

    return redirect(request.META.get('HTTP_REFERER', '/'))
