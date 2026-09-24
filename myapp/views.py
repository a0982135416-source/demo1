from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7a9cde8daf2894d94c46dc0ce81a958e49566d20


# def home(request):
#     return render(request, 'index.html')
def aweb(request):
    return HttpResponse("aweb.html完成")
=======

def home(request):
    return render(request, 'index.html')
<<<<<<< HEAD
def cweb(request):
    return HttpResponse("This is the cweb page.完成")
=======


def about(request):
    return HttpResponse("This is the about page.")

def cweb(request):
    return HttpResponse("This is the cweb page.完成")
>>>>>>> origin/main
>>>>>>> 7a9cde8daf2894d94c46dc0ce81a958e49566d20
