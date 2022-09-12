from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *
from .forms import *


def user_contact(request, pk):
    user = request.user.id
    instance = Contacts.objects.filter(pk=pk, user_id=user).first()
    if request.method == 'GET':
        if instance is None:
            return redirect('contact_list')
        form = ContactForm(instance=instance)
        return render(request, "contacts/edit_contact.html", {'form': form})
    if request.method == 'POST':
        if request.POST.get('b-delete') == 'delete':
            instance.delete()
            return redirect('contact_list')
        form = ContactForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        return render(request, 'contacts/edit_contact.html', {'form': form})


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            email_one = form.cleaned_data['email_one']
            phone = form.cleaned_data['phone']
            phone_one = form.cleaned_data['phone_one']
            address = form.cleaned_data['address']
            user = request.user.id
            contact = Contacts.objects.filter(name=name, user_id=user).first()
            if contact is None:
                if birthday == '':
                    contact = Contacts.objects.create(
                        name=name,
                        address=address,
                        email=email,
                        email_one=email_one,
                        phone=phone,
                        phone_one=phone_one,
                        user_id=user
                    )
                else:
                    contact = Contacts.objects.create(
                        name=name,
                        birthday=birthday,
                        address=address,
                        email=email,
                        email_one=email_one,
                        phone=phone,
                        phone_one=phone_one,
                        user_id=user
                    )
                contact.save()
                messages.success(request, 'Success create')
                return redirect('create_contact')
            else:
                messages.error(request, 'Contact name already exist!')
        else:
            messages.error(request, 'Error valid from')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


class ContactByUser(ListView):
    model = Contacts
    template_name = 'contacts/contacts_view.html'
    context_object_name = 'contacts_data'

    def get_queryset(self):
        return Contacts.objects.filter(user_id=self.request.user.id)


class Search(ListView):
    template_name = 'contacts/contacts_view.html'
    context_object_name = 'contacts_data'

    def get_queryset(self):
        if self.request.GET.get('s') is None:
            return None
        return Contacts.objects.filter(
            Q(name__icontains=self.request.GET.get('s'), user_id=self.request.user.id) |
            Q(phone__icontains=self.request.GET.get('s'), user_id=self.request.user.id) |
            Q(phone_one__icontains=self.request.GET.get('s'), user_id=self.request.user.id) |
            Q(email__icontains=self.request.GET.get('s'), user_id=self.request.user.id) |
            Q(email_one__icontains=self.request.GET.get('s'), user_id=self.request.user.id))
