from django.shortcuts import render, redirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    markdown_result = util.get_entry(entry)
    if markdown_result is not None:
        return render(request, "encyclopedia/entry.html", {
            "name": entry,
            "entry": markdown_result
        })
    else:
        return render(request, "encyclopedia/no_entry.html", {
            "name": entry
        })
    

def search(request):
    search = request.POST.get('q')
    if search != "":
        equal_to_entry = [entry for entry in util.list_entries() if entry.lower() == search.lower()]
        if equal_to_entry:
            return redirect('entry', entry=equal_to_entry[0])
        in_entry = [entry for entry in util.list_entries() if search.lower() in entry.lower()]
        if in_entry:
            return render(request, "encyclopedia/search.html", {
                "search": search,
                "entries": in_entry              
            })
    return render(request, "encyclopedia/no_search_match.html", {
        "search": search
    })


def random_entry(request):
    entries = util.list_entries()
    random_number = random.uniform(0, len(entries) - 1)
    random_entry = entries[int(random_number)]
    return redirect('entry', entry=random_entry)


