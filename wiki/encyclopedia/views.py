from django.shortcuts import render, redirect
import random
import re

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


def create_entry(request):
    return render(request, "encyclopedia/create_entry.html")


def save_new(request):
    entries = [e.lower() for e in util.list_entries()]
    entry_name = request.POST.get('name')
    entry_content = request.POST.get('content')
    if entry_name.lower() in entries:
        return render(request, "encyclopedia/entry_already_exists.html", {
            "entry": entry_name
        })
    elif entry_name == "":
        return render(request, "encyclopedia/empty_entry.html")
    else:
        with open("entries/" + entry_name + ".md", 'w') as file:
            file.write(entry_content)
        return redirect('entry', entry=entry_name)
    

def edit_entry(request):
    entry_name_in_url = request.POST.get("current_url")
    entry_name_in_url = entry_name_in_url.replace('/wiki/', '')
    entry_name = entry_name_in_url.lower().replace("%20", " ")
    entry_name = [e for e in util.list_entries() if e.lower() == entry_name][0]
    entry_content = util.get_entry(entry_name, to_html=False)
    if isinstance(entry_content, (tuple, list)):
        entry_content = "".join(entry_content)
    match = re.search(r"#", entry_content)
    entry_content = entry_content[match.start():]
    return render(request, "encyclopedia/edit_entry.html", {
        "entry": entry_name,
        "content": entry_content
    })


def save_edit(request):
    entry_name = request.POST.get("name")
    content = request.POST.get("content")
    util.save_entry(entry_name, content)
    if isinstance(content, (tuple, list)):
        content = "".join(content)
    match = re.search(r"#", content)
    content = content[match.start():]
    return redirect('entry', entry=entry_name)




