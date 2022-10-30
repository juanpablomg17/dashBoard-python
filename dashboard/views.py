from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Death, Birth, Education
from .forms import ProductForm, BirthForm, EducationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    customer = User.objects.filter(groups=2)
    death = Death.objects.all()
    birth = Birth.objects.all()
    education = Education.objects.all()
    
    death_count = death.count()
    birth_count = birth.count()
    education_count = education.count()
    
    
    customer_count = customer.count()

    form = ProductForm()
    context = {
        'form': form,
        'death': death,
        'birth': birth,
        'education': education,
        
        'death_count': death_count,
        'birth_count': birth_count,
        'education_count': education_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def deaths(request):
    death = Death.objects.all()
    death_count = death.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('year')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-deaths')
    else:
        form = ProductForm()
    context = {
        'death': death,
        'form': form,
        'customer_count': customer_count,
        'death_count': death_count,
    }
    return render(request, 'dashboard/death.html', context)

@login_required(login_url='user-login')
def births(request):
    birth = Birth.objects.all()
    birth_count = birth.count()
    if request.method == 'POST':
        form = BirthForm(request.POST)
        if form.is_valid():
            form.save()
            birth_year = form.cleaned_data.get('year')
            messages.success(request, f'{birth_year} has been added')
            return redirect('dashboard-births')
    else:
        form = BirthForm()
    context = {
        'birth': birth,
        'form': form,
        'birth_count': birth_count,
    }
    return render(request, 'dashboard/birth.html', context)

@login_required(login_url='user-login')
def educations(request):
    education = Education.objects.all()
    education_count = education.count()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            education_year = form.cleaned_data.get('year')
            messages.success(request, f'{education_year} has been added')
            return redirect('dashboard-educations')
    else:
        form = EducationForm()
    context = {
        'education': education,
        'form': form,
        'education_count': education_count,
    }
    return render(request, 'dashboard/education.html', context)


@login_required(login_url='user-login')
def death_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/death_detail.html', context)

@login_required(login_url='user-login')
def birth_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/birth_detail.html', context)

@login_required(login_url='user-login')
def education_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/education_detail.html', context)


@login_required(login_url='user-login')
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    death = Death.objects.all()
    death_count = death.count()
    
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'death_count': death_count,
    }
    return render(request, 'dashboard/customers.html', context)


@login_required(login_url='user-login')
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    death = Death.objects.all()
    death_count = death.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'death_count': death_count,
    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required(login_url='user-login')
def death_edit(request, pk):
    item = Death.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-deaths')    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/deaths_edit.html', context)


@login_required(login_url='user-login')
def birth_edit(request, pk):
    item = Birth.objects.get(id=pk)
    if request.method == 'POST':
        form = BirthForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-births')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/birth_edit.html', context)


@login_required(login_url='user-login')
def education_edit(request, pk):
    item = Education.objects.get(id=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-educations')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/education_edit.html', context)





@login_required(login_url='user-login')
def death_delete(request, pk):
    item = Death.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-deaths')
    context = {
        'item': item
    }
    return render(request, 'dashboard/deaths_delete.html', context)


@login_required(login_url='user-login')
def birth_delete(request, pk):
    item = Birth.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-births')
    context = {
        'item': item
    }
    return render(request, 'dashboard/deaths_delete.html', context)

@login_required(login_url='user-login')
def education_delete(request, pk):
    item = Education.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-educations')
    context = {
        'item': item
    }
    return render(request, 'dashboard/education_delete.html', context)