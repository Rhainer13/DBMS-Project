from django.shortcuts import render, redirect
from .models import Resident
from .forms import ResidentForm
from django.contrib import messages

# Create your views here.
def index(request):
    resident_count = Resident.objects.count()
    male_residents = Resident.objects.filter(gender='Male').count()
    female_residents = Resident.objects.filter(gender='Female').count()

    context = {
        'resident_count': resident_count,
        'male_residents': male_residents,
        'female_residents': female_residents,
    }
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
            first_name = form.cleaned_data['first_name'].lower()
            middle_name = form.cleaned_data['middle_name'].lower()
            last_name = form.cleaned_data['last_name'].lower()
            birth_date = form.cleaned_data['birth_date']
            phone_number = form.cleaned_data['phone_number']

            if Resident.objects.filter(first_name=first_name, middle_name=middle_name, last_name=last_name, birth_date=birth_date).exists():
                messages.error(request, 'Resident already exists.')
            elif Resident.objects.filter(phone_number=phone_number).exists():
                messages.error(request, 'Phone Number already exists.')
            else:
                Resident.objects.create(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    birth_date=birth_date,
                    gender=form.cleaned_data['gender'], 
                    purok=form.cleaned_data['purok'], 
                    phone_number=form.cleaned_data['phone_number']
                )
                messages.success(request, f'Resident {first_name.capitalize()} {last_name.capitalize()} has been added successfully.')
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
            first_name = form.cleaned_data['first_name'].lower()
            middle_name = form.cleaned_data['middle_name'].lower()
            last_name = form.cleaned_data['last_name'].lower()
            birth_date = form.cleaned_data['birth_date']
            phone_number = form.cleaned_data['phone_number']

            # Check for duplicate resident
            if Resident.objects.filter(first_name=first_name, middle_name=middle_name, last_name=last_name, birth_date=birth_date).exclude(id=pk).exists():
                messages.error(request, 'Resident with the same name and birth date already exists.')
            elif Resident.objects.filter(phone_number=phone_number).exclude(id=pk).exists():
                messages.error(request, 'Phone Number already exists.')
            else:
                form.save()
                messages.success(request, f'Resident {first_name.capitalize()} {last_name.capitalize()} has been updated successfully.')
                return redirect('barangay-residents')
    context = {
        'form':form,
    }
    return render(request, 'app1/update-resident.html', context)

def delete_resident(request, pk):
    resident = Resident.objects.get(id=pk)
    form = ResidentForm(instance=resident)

    first_name = resident.first_name
    last_name = resident.last_name

    if request.method == 'POST':
        resident.delete()
        messages.success(request, f'Resident {first_name.capitalize()} {last_name.capitalize()} has been deleted successfully.')
        return redirect('barangay-residents')
    
    context = {
        'form':form,
    }

    return render(request, 'app1/delete-resident.html', context)