from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'public/index.html', context)


def register(request):
    context = {}
    return render(request, 'public/register.html', context)