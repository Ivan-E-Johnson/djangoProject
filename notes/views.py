from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView

from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model= Notes
    success_url = '/smart/notes'#redirect user to existing notes
    form_class= NotesForm

class NotesCreateView(CreateView):
    model= Notes
    success_url = '/smart/notes'#redirect user to existing notes
    form_class= NotesForm



class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

