from django.shortcuts import render
from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    markdowner = Markdown()
    return render(request, "encyclopedia/page.html",{
        "page": markdowner.convert(util.get_entry(request.POST.get("page")))
    })