from django.shortcuts import render

# Create your views here.

from .models import ContactBook

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm
from django.db.models import Q 

class HomeView(ListView):
    model=ContactBook
    template_name="App_Contact/home.html"
    context_object_name = 'contacts'
    
class ContactDetailView(DetailView):
    model=ContactBook
    template_name="App_Contact/detail.html"
    
class ContactAddView(CreateView):
    model = ContactBook
    form_class = ContactForm
    template_name = 'App_Contact/create.html'
    success_url = reverse_lazy('home')
    
class EditContact(UpdateView):
    model=ContactBook 
    fields = ['first_name', 'last_name', 'email', 'phone', 'address']
    template_name="App_Contact/edit.html"
    success_url="/"
    
class DeleteContact(DeleteView):
    model=ContactBook 
    template_name="App_Contact/delete.html"
    success_url="/"
    
class ContactSearchView(ListView):
    model = ContactBook
    template_name = 'App_Contact/search.html'
    context_object_name = 'contacts'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return ContactBook.objects.filter(Q(first_name__icontains=query) | Q(email__icontains=query))
        else:
            return ContactBook.objects.all() 