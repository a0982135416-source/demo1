from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
def aweb(request):
    return render(request, 'aweb.html')