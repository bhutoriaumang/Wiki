from django.shortcuts import render,redirect
from . import util
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request):
    path = "/encyclopedia/"+request.GET.get("page")
    return redirect(path)

def entry(request,entry):
    markdowner = Markdown()
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/page.html",{
        "page": markdowner.convert(util.get_entry(entry)),
        "entry": entry
    })