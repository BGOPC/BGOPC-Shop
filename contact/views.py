from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':
        cf = ContactForm(request.POST)
        if cf.is_valid():
            obj = Contact.objects.create(
                name=request.POST['name'], title=request.POST['title'], email=request.POST['email'], message=request.POST['message'])
            obj.save()
            return redirect(reverse('response', kwargs={'cid': obj.id}))
    cf = ContactForm()
    return render(request, 'contact/contact.html', {
        'contact_form': cf
    })


def response(request, cid):
    costumer = get_object_or_404(Contact, id=cid)
    return render(request, 'contact/response.html', {
        'costumer': costumer,
    })

def about(request):
    return render(request, 'contact/about.html')