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
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/page.html",{
        "page": markdowner.convert(entries[entry.lower()]),
        "entry": entry
    })

def create(request):
    return render(request,"encyclopedia/create.html")

def createpage(request):
    util.save_entry(request.GET.get("title"),request.GET.get("content"))
    return redirect("/encyclopedia/")

def random(request):
    l = []
    for i in entries:
        l.append(i)
    path = "/encyclopedia/"+(sample(l,1)[0])+"/"
    return redirect(path)
