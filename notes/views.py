from django.shortcuts import render, redirect
from .models import Note, Tag

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("titulo")
        content = request.POST.get("detalhes")
        tag_title = request.POST.get("tag")
        if tag_title == "":
            note = Note(title=title, content=content)
            note.save()
            return redirect("index")
        else:
            tag = Tag(title=f"#{tag_title}")
            lista_tag_igual = Tag.objects.filter(title=f"#{tag_title}")
            if not lista_tag_igual:
                tag.save()
            else: 
                tag = lista_tag_igual[0]
            note = Note(title=title, content=content, tag=tag)
            note.save()
            return redirect("index")
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, id):
    Note.objects.filter(id=id).delete()
    return redirect("index")

def edit(request, id):
    edit_note = Note.objects.get(id=id)
    if request.method == "POST":
        edit_note.title = request.POST.get("titulo")
        edit_note.content = request.POST.get("detalhes")
        tag_title = request.POST.get('tag')
        
        tag = Tag(title=f"#{tag_title}")
        lista_tag_igual = Tag.objects.filter(title=f"#{tag_title}")
        if not lista_tag_igual:
            tag.save()
        else: 
            tag = lista_tag_igual[0]

        edit_note.tag = tag
        edit_note.save()
        return redirect("index")
    else:
        return render(request, 'notes/edit.html', {'note': edit_note})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, "notes/tags.html", {'tags': all_tags})

def note_tags(request, id):
    note_with_tag = Note.objects.all().filter(tag_id = id)
    return render(request, "notes/note_tags.html", {'notes': note_with_tag})