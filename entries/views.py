from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name='entries/index.html'
    context_object_name="blog_entries"
    ordering=['-entry_date']
    paginate_by=4

class EntryView(DetailView):
    model = Entry
    template_name='entries/entry_detail.html'
