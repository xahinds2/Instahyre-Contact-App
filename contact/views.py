from contact.models import Contact
from django.shortcuts import render, redirect


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
