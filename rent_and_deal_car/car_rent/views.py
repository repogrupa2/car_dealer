from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import RentalOffer
from .models import CarAvailability
from .models import Branch
from .forms import RentalOfferCreate
from .forms import CarAvailabilityCreate
from .forms import BranchCreate



def list_of_branch(request):
    list_of_branches = Branch.objects.all()
    return render(request, 'car_rent/list_of_branches.html', {'list_of_branches': list_of_branches})


def create_branch(request):
    form = BranchCreate()
    if request.method == 'POST':
        form = BranchCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_rent:list-of-branch')

    ctx={'form':form}
    return render(request, 'car_rent/create_branch.html', ctx)


def edit_branch(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    form = BranchCreate(instance=branch)
    if request.method == 'POST':
        form = BranchCreate(request.POST,instance=branch)
        if form.is_valid():
            form.save()
            return redirect('car_rent:list-of-branch')

    ctx = {'form': form}
    return render(request, 'car_rent/create_branch.html',ctx)

def delete_branch(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    if request.method == 'POST':
        branch.delete()
        return redirect('car_rent:list-of-branch')

    ctx={'item':branch}
    return render(request, 'car_rent/delete_branch.html', ctx)


def get_branch(request, branch_id):
    try:
        branch = Branch.objects.get(id=branch_id)
    except Branch.DoesNotExist:
        ctx = {'branch': branch}

    ctx = {'branch': branch}
    return render(request, "car_rent/branch.html", context=ctx)


def list_of_rental_offers(request):
    Offer = RentalOffer.objects.all()
    return render(request, 'car_rent/list_of_offers.html', {'offer': Offer})


def get_offer(request, RentalOffer_id):
    try:
        offer = RentalOffer.objects.get(id=RentalOffer_id)
    except RentalOffer.DoesNotExist:
        ctx = {'offer': offer}

    ctx = {'offer': offer}
    return render(request, "car_rent/offer.html", context=ctx)


def upload_offer(request):
    upload = RentalOfferCreate()
    if request.method == 'POST':
        upload = RentalOfferCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('list_of_offers')
        else:
            return HttpResponse()
    else:
        return render(request, 'car_rent/create_offer.html',{'create_offer':upload})

def update_RentalOffer(request, RentalOffer_id):
    RentalOffer_id = int(RentalOffer_id)
    try:
        RentalOffer_sel = RentalOffer.objects.get(id = RentalOffer_id)
    except RentalOffer.DoesNotExist:
        return redirect('list_of_offers')
    RentalOffer_form = RentalOfferCreate(request.POST or None, instance = RentalOffer_sel)
    if RentalOffer_form.is_valid():
       RentalOffer_form.save()
       return redirect('list_of_offers')
    return render(request, 'RentalOffer/upload_form.html', {'upload_form':RentalOffer_form})

def delete_RentalOffer(request, RentalOffer_id):
    RentalOffer_id = int(RentalOffer_id)
    try:
        RentalOffer_sel = RentalOffer.objects.get(id = RentalOffer_id)
    except RentalOffer.DoesNotExist:
        return redirect('list_of_offers')
    RentalOffer_sel.delete()
    return redirect('list_of_offers')
