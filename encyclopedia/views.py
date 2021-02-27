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
    #return entry(request,request.GET.get("page"))
    #markdowner = Markdown()
    #return render(request, "encyclopedia/page.html",{
    #    "page": markdowner.convert(util.get_entry(request.GET.get("page")))
    #})

def entry(request,entry):
    markdowner = Markdown()
    return render(request, "encyclopedia/page.html",{
        "page": markdowner.convert(util.get_entry(entry))
    })