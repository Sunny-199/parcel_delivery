# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from users.models import Contacts
# Create your views here.


class DashboardView(TemplateView):
    template_name = "account/dashboard.html"


class ShipmentsView(TemplateView):
    template_name = "account/shipments.html"


# class AddressView(TemplateView):
#     print("*****************************************************************")
#     template_name = "account/addresses.html"
def address_view(request):
    contact_list = Contacts.objects.all()
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'account/addresses.html', context)


class TicketsView(TemplateView):
    template_name = "account/tickets.html"


class DetailView(TemplateView):
    template_name = "account/detail.html"


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        apartment_suit = request.POST['apartment_suit']
        city = request.POST['city']
        country = request.POST['country']
        province = request.POST['province']
        postal = request.POST['postal']
        contact = Contacts.objects.create(name=name,address=address, apartment_suit=apartment_suit, city=city,
                                         country=country, province=province, postal=postal)
        contact_list = Contacts.objects.all()
    contact_list = Contacts.objects.all()
    print(contact_list)
    context = {
        "contact_list": contact_list,
    }
    return render(request, 'account/addresses.html', context)


def Address(request):
    contact_list = Contacts.objects.all()
    print(contact_list)
    context = {
        "contact_list": contact_list,
    }
    return render(request, 'components/address_map.html', context)


