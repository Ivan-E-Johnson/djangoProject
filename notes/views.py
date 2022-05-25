from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView
from django.views.generic import DetailView

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


def detail(request, pk):
    try:
        note = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(request, 'notes/notes_detail.html',{'note': note})