from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'app1/index.html', context)

def residents(request):
    context = {}
    return render(request, 'app1/residents.html', context)