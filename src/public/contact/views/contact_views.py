from django.shortcuts import render
from ..models import Contact
# Create your views here.

def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')
    context = {
        'contacts': contacts,
    }
    print(contacts)
    return render(request,
                  'contact/index.html',
                  context)