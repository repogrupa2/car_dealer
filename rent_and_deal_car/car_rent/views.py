from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import CustomUserCompleteDetails, PaymentForm
from .models import Branch, Vehicle, Brand, Model, RentalOffer, CarRental, BranchCarAvailability, CustomUser
import datetime

User = get_user_model()


def home(request):
    vehicles = Vehicle.objects.all()
    ctx = {'vehicles': vehicles}

    return render(request, "car_rent/home.html", context=ctx)


def aboutus(request):
    return render(request, "car_rent/about_us.html")


class AccountDetails(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)

        account = [user.first_name, user.last_name, user.street, user.house_number,
                   user.zip_code, user.city, user.credit_card_nr, user.mobile]
        count = 0
        for i in account:
            # print(i)
            if len(str(i)) is 0 or i is None:
                count += 1
        if count > 0:
            ctx = {'user': user, 'count': count}
        else:
            ctx = {'user': user}
        return render(self.request, "car_rent/account_details.html", context=ctx)


class AdminPanel(View):
    def get(self, request, *args, **kwargs):
        return render(request, "admin")


class ListOfBranches(View):
    def get(self, request, *args, **kwargs):
        list_of_branches = Branch.objects.all()
        ctx = {'list_of_branches': list_of_branches}
        return render(self.request, 'car_rent/list_of_branches.html', context=ctx)


class ViewBranch(View):
    def get(self, request, branch_id, *args, **kwargs):
        try:
            branch = Branch.objects.get(id=branch_id)
            ctx = {"branch": branch}
        except Branch.DoesNotExist:
            ctx = {'branch_id': id}
        return render(request, "car_rent/branch.html", context=ctx)


class ListOfRentalOffers(View):
    def get(self, request, *args, **kwargs):
        list_of_offers = RentalOffer.objects.all()
        vehicles = Vehicle.objects.all()
        user = CustomUser.objects.get(id=request.user.id)
        car_rentals = CarRental.objects.filter(customer_id=user.id)

        for customer_record in car_rentals:
            if customer_record.is_rented:
                ctx = {'list_of_offers': list_of_offers, 'rented': customer_record.rental_offer_id.id}
                return render(request, "car_rent/list_of_offers.html", context=ctx)

        ctx = {'list_of_offers': list_of_offers, 'vehicles': vehicles}
        return render(self.request, 'car_rent/list_of_offers.html', context=ctx)


class RentalOfferView(View):
    def get(self, request, rental_offer_id, *args, **kwargs):
        try:
            rental_offer = RentalOffer.objects.get(id=rental_offer_id)
            vehicles = Vehicle.objects.all()
            ctx = {"rental_offer": rental_offer, 'vehicles': vehicles}
        except RentalOffer.DoesNotExist:
            ctx = {'rental_offer_id': id}
        return render(request, "car_rent/offer.html", context=ctx)


class VehicleList(View):
    def get(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.all()
        ctx = {'vehicles': vehicles}
        return render(self.request, "car_rent/vehiclelist.html", context=ctx)


class BrandList(View):
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.all()
        ctx = {'brand': brand}

        return render(self.request, "car_rent/brand_list.html", context=ctx)


class ModelList(View):
    def get(self, request, *args, **kwargs):
        model = Model.objects.all()
        ctx = {'model': model}

        return render(self.request, "car_rent/model_list.html", context=ctx)


class CarRentalDetails(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)
            car_availability = BranchCarAvailability.objects.get(vehicle_id=offer.Vehicle_Id)

        except RentalOffer.DoesNotExist:
            return HttpResponse()

        except BranchCarAvailability.DoesNotExist:
            return HttpResponse()

        date = datetime.date.today()
        '''Take loged user'''
        user = CustomUser.objects.get(id=request.user.id)
        '''Take all record for user who rent any car'''
        car_rentals = CarRental.objects.filter(customer_id=user.id)

        for customer_record in car_rentals:
            '''
            If the user is still renting any car then return rented is True then not have option to rent
            '''
            if customer_record.is_rented:
                ctx = {"offer": offer, "date": date, 'rented': True}
                return render(request, "car_rent/car_rental.html", context=ctx)

        ctx = {"offer": offer, "date": date}
        return render(request, "car_rent/car_rental.html", context=ctx)

    def post(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)
            availability = BranchCarAvailability.objects.get(vehicle_id=offer.Vehicle_Id)
            user = CustomUser.objects.get(id=request.user.id)

        except RentalOffer.DoesNotExist:
            return HttpResponse()

        except BranchCarAvailability.DoesNotExist:
            return HttpResponse()

        ctx = {'offer': offer, 'user': user}

        if user.balance - offer.Deposit >= 0:
            user.balance -= offer.Deposit
            car_rental = CarRental.objects.create(customer_id=user, rental_offer_id=offer, is_rented=True)
            availability.availability = False
            user.save()
            car_rental.save()
            availability.save()


            return render(request, "car_rent/car_rental_succusfull.html", context=ctx)

        else:
            messages.info(self.request, "You haven't enough cash to pay deposit for car, on your account. ")
            return render(self.request, "car_rent/car_rental.html", context=ctx)




def date_counter(date_of_rent):
    """Date Counter when car is returned"""
    today = datetime.date.today()
    time_rent = today - date_of_rent
    return time_rent.days + 1


class ReturnCar(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)
            car_availability = BranchCarAvailability.objects.get(vehicle_id=offer.Vehicle_Id)

        except RentalOffer.DoesNotExist:
            return HttpResponse()

        except BranchCarAvailability.DoesNotExist:
            return HttpResponse()

        user = CustomUser.objects.get(id=request.user.id)
        car_rental = CarRental.objects.get(customer_id=user, rental_offer_id=offer, is_rented=True)
        date = datetime.date.today()
        total_price = date_counter(car_rental.date_of_rent) * offer.Price_per_day

        ctx = {"offer": offer, "date": date, 'total_price': total_price}
        return render(request, "car_rent/car_rental_return.html", context=ctx)

    def post(self, request, id, *args, **kwargs):
        try:
            offer = RentalOffer.objects.get(id=id)
            availability = BranchCarAvailability.objects.get(vehicle_id=offer.Vehicle_Id)

        except RentalOffer.DoesNotExist:
            return HttpResponse()

        except BranchCarAvailability.DoesNotExist:
            return HttpResponse()

        user = CustomUser.objects.get(id=request.user.id)
        car_rental = CarRental.objects.get(customer_id=user, rental_offer_id=offer, is_rented=True)
        car_rental.is_rented = False
        availability.availability = True
        total_price = date_counter(car_rental.date_of_rent) * offer.Price_per_day
        user.balance += offer.Deposit
        user.balance -= total_price

        user.save()
        car_rental.save()
        availability.save()

        ctx = {"offer": offer, 'user': user, 'total_price': total_price}
        return render(request, "car_rent/car_rental_return_successful.html", context=ctx)


class CompleteDetails(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        form = CustomUserCompleteDetails()
        ctx = {"form": form}
        return render(request, "car_rent/account_complete_details.html", context=ctx)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        form = CustomUserCompleteDetails(data=request.POST)
        if form.is_valid():

            user.street = form.cleaned_data["street"]
            user.house_number = form.cleaned_data["house_number"]
            user.zip_code = form.cleaned_data["zip_code"]
            user.city = form.cleaned_data["city"]
            user.credit_card_nr = form.cleaned_data["credit_card_nr"]
            user.expiration = form.cleaned_data["expiration"]
            user.CVV = form.cleaned_data["CVV"]
            user.mobile = form.cleaned_data["mobile"]

            user.save(update_fields=["street", "house_number", "zip_code", "city",
                                     "credit_card_nr", 'expiration', 'CVV', 'mobile'])

            ctx = {"form": form, "user": user}
            return render(request, "car_rent/account_complete_details.html", context=ctx)
        return HttpResponse()


class AccountPayment(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form = PaymentForm()
        ctx = {'form': form, 'user': user}
        return render(request, "car_rent/account_payment.html", context=ctx)

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            if int(form.cleaned_data['credit_card_nr']) == user.credit_card_nr:
                if authenticate(username=user.email, password=form.cleaned_data['password']):
                    user.balance = user.balance + form.cleaned_data['balance']
                    user.save()
                    messages.info(request, f"Excellent !!! The amount {form.cleaned_data['balance']} has been paid")
                    return render(self.request, "car_rent/account_payment.html",
                                  context={'form': form, 'good_message': True})
                else:
                    messages.info(self.request, 'Password is not correct')
                    return render(self.request, "car_rent/account_payment.html", context={'form': form})

            else:
                messages.info(request, 'Credit card is not correct')
                return render(request, "car_rent/account_payment.html", context={'form': form})
        else:
            messages.info(request, 'Oops, some problem try again or come back later')
            return render(request, "car_rent/account_payment.html", context={'form': form})