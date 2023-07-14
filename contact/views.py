from django.contrib.auth.decorators import login_required
from django.db import DataError, IntegrityError
from faker import Faker
from contact.models import Contact
from django.shortcuts import render, redirect
from ordered_set import OrderedSet
from home.models import CustomUser

fake = Faker()


@login_required
def my_contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        Contact.objects.create(name=name, mobile=mobile, email=email, owner=request.user)

    context = {
        'contacts': Contact.objects.all().values()
    }

    return render(request, 'my_contacts.html', context)


@login_required
def search_contacts(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        user = CustomUser.objects.filter(mobile=query).first()

        contacts = []

        if user:
            contact = Contact.objects.filter(mobile=user.mobile, owner=request.user).first()
            if contact:
                contact.name = user.name
                contact.email = user.email
            else:
                contact = Contact.objects.create(name=user.name, mobile=user.mobile, owner=request.user)

            contacts = [contact]

        elif query:
            contacts += Contact.objects.filter(mobile=query)
            contacts += Contact.objects.filter(name__startswith=query)
            contacts += Contact.objects.filter(name__icontains=query)
            for i in range(len(contacts)):
                contacts[i].email = ''

        context = {
            'contacts': OrderedSet(contacts),
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
        s = fake.phone_number()
        mobile = "".join(c for c in s if c.isnumeric())
        email = fake.email()
        _spam = fake.pybool()
        try:
            Contact.objects.create(name=name, mobile=mobile, email=email, spam=_spam, owner=request.user)
        except DataError:
            pass

    return redirect(request.META.get('HTTP_REFERER', '/'))
