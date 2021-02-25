from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    return render(request, "encyclopedia/page.html",{
        "page": util.get_entry(request.POST.get("page"))
    })