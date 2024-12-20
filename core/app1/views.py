from django.shortcuts import render, redirect
from .models import Resident
from .forms import ResidentForm
from django.contrib import messages
from datetime import date, timedelta
from django.db.models import Q

# Create your views here.
def index(request):
    resident_count = Resident.objects.count()
    male_residents = Resident.objects.filter(gender='Male').count()
    female_residents = Resident.objects.filter(gender='Female').count()

    # Calculate the date 60 years ago from today
    sixty_years_ago = date.today() - timedelta(days=60*365.25)
    senior_residents = Resident.objects.filter(birth_date__lte=sixty_years_ago).count()

    # Calculate the date 18 years ago from today
    eighteen_years_ago = date.today() - timedelta(days=18*365.25)
    # Filter residents aged 18 to 59
    adult_residents = Resident.objects.filter(birth_date__gt=sixty_years_ago, birth_date__lte=eighteen_years_ago).count()
    
    # Filter residents less than 18 years old
    child_residents = Resident.objects.filter(birth_date__gt=eighteen_years_ago).count()

    context = {
        'resident_count': resident_count,
        'male_residents': male_residents,
        'female_residents': female_residents,
        'child_residents': child_residents,
        'adult_residents': adult_residents,
        'senior_residents': senior_residents,
    }
    return render(request, 'app1/index.html', context)

def residents(request):
    q = request.GET.get('q')

    if q:
        residents = Resident.objects.filter(
            Q(first_name__icontains=q) |
            Q(middle_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(phone_number__icontains=q)
        )
    else:
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

def medicine_inventory(request):
    context = {

    }
    return render(request, 'app1/medicine-inventory.html', context)