from django.shortcuts import render

# Create your views here.

def bootstrap_dwnld(request):
    return render(request, 'bootstrap_dwnld.html')