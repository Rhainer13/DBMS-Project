from django.shortcuts import render, redirect
from .models import Resident
from .forms import ResidentForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'app1/index.html', context)

def residents(request):
    residents = Resident.objects.all()
    resident_count = Resident.objects.count()

    context = {
        'residents': residents, 
        'resident_count': resident_count,
    }
    return render(request, 'app1/residents.html', context)

def add_resident(request):
    form = ResidentForm()

    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barangay-residents')

    context = {
        'form':form,
    }
    return render(request, 'app1/add-resident.html', context)

def update_resident(request, pk):
    resident = Resident.objects.get(id=pk)
    form = ResidentForm(instance=resident)

    if request.method == 'POST':
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('barangay-residents')

    context = {
        'form':form,
    }
    return render(request, 'app1/add-resident.html', context)