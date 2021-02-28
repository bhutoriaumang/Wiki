from django.shortcuts import render,redirect
from . import util
from markdown2 import Markdown
from random import sample

entries = {}

def index(request):
    for i in util.list_entries():
        entries[i.lower()] = util.get_entry(i)
    l = []
    for i in util.list_entries():
        l.append(i)
    return render(request, "encyclopedia/index.html", {
        "entries": l
    })

def page(request):
    path = "/encyclopedia/"+request.GET.get("page")+"/"
    return redirect(path)

def entry(request,entry):
    markdowner = Markdown()
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html",{
            "msg": "Page not found !"
        })
    return render(request, "encyclopedia/page.html",{
        "page": markdowner.convert(entries[entry.lower()]),
        "entry": entry
    })

def create(request):
    return render(request,"encyclopedia/create.html")

def createpage(request, flag):
    title = request.GET.get("title")
    if title in util.list_entries() and flag == "True":
        return render(request, "encyclopedia/error.html",{
            "msg": "A page with the same name already exisits !"
        })
    else:
        markdowner = Markdown()
        util.save_entry(title,request.GET.get("content"))
        entries[title.lower()] = util.get_entry(title)
        path = "/encyclopedia/"+title+"/"
        return redirect(path, {
            "page": markdowner.convert(util.get_entry(title)),
            "entry": title
        })

def edit(request, entry):
    if not entry.lower() in entries:
        return render(request, "encyclopedia/error.html", {
            "msg": "Invalid Request !"
        })
    content = entries[entry.lower()]
    content = content[content.index("\n")+1:]
    return render(request, "encyclopedia/edit.html", {
        "title": entry,
        "content": content
    })

def random(request):
    l = []
    for i in entries:
        l.append(i)
    path = "/encyclopedia/"+(sample(l,1)[0])+"/"
    return redirect(path)
