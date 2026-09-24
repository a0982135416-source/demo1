from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("This is the about page.")

def cweb(request):
    return HttpResponse("This is the cweb page.完成")
