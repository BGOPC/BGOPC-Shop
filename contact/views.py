from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST' and request.POST['name'] != '':
        st = True
        for v in request.POST.values():
            if v in (''):
                st = False
                break
        if st:
            obj = Contact.objects.create(
                name=request.POST['name'], title=request.POST['title'], email=request.POST['email'], message=request.POST['message'])
            obj.save()
            return redirect(reverse('response', kwargs={'cid': obj.id}))

    return render(request, 'contact/contact.html',)


def response(request, cid):
    costumer = get_object_or_404(Contact, id=cid)
    return render(request, 'contact/response.html', {
        'costumer': costumer,
    })
