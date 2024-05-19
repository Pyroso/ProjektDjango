from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from aplikacja.form import NotatkaForm
from aplikacja.models import Notatka
from django.views.generic import ListView



# Create your views here.
# def note_list(request):
#     notes = Notatka.objects.all()
#     return render(request, "post/list.html",{"notes":notes})
# Create your views here.
class NoteListView(ListView):
    queryset = Notatka.objects.all().filter(status__in = ('wazne','mniejwazne')).order_by('-status')
    context_object_name = 'notes'
    paginate_by = 3
    template_name = "post/list.html"
def note_detail(request, year, month, day):
    note = get_object_or_404(Notatka,
                             status__in = ('wazne','mniejwazne'),
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    return render(request, "post/detail.html",
                  {'note': note,})
def create_note(request):
    if request.method == 'POST':
        form = NotatkaForm(request.POST)
        if form.is_valid(): # sprawdzenie czy formularz jest wlasciwy
            note = form.save(commit=False)
            note.author = User.objects.get(id=1)
            note.save()
            return redirect('aplikacja:note_detail', year=note.created.year, month=note.created.strftime('%m'),
                            day=note.created.strftime('%d'))
    else:
        form = NotatkaForm()
    return render(request, 'Strony/create.html', {'form': form})


def edit_note(request, note_id):
    note = get_object_or_404(Notatka, pk=note_id)
    if request.method == 'POST':
        form = NotatkaForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('aplikacja:note_detail', year=note.created.year, month=note.created.strftime('%m'),
                            day=note.created.strftime('%d'))
    else:
        form = NotatkaForm(instance=note)
    return render(request, 'Strony/edit.html', {'form': form,'note':note})
