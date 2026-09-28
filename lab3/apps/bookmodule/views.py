from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def viewbook(request, bookId):
    b1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble'}
    b2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    target = None
    if bookId == 123:
        target = b1
    elif bookId == 456:
        target = b2

    return render(request, 'bookmodule/show.html', {'book': target})